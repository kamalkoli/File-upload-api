from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.serializer import MegazineCategoriesSerializer, MegazineDetailsSerializer, MegazinePagesSerializer
from rest_framework.parsers import MultiPartParser


class MegazineCategoriesView(APIView):
     def post(self, request):
        serializer = MegazineCategoriesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Data Saved Successfully.', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class MegazineDetailsView(APIView):
    def post(self, request):
        serializer = MegazineDetailsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Data Saved Successfully.', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class MegazinePagesView(APIView):
    parser_class = (MultiPartParser,)
    def post(self, request):
        check_serializer = MegazinePagesSerializer(data=request.data)
        try:
            if check_serializer.is_valid:
                files = request.FILES.getlist('MegazinePages')
                MegId = request.data['MegazineID']
                dic ={}
                for value in files:
                    print(value, '======')
                    dic['MegazinePages'] = value
                    dic['MegazineID'] = MegId
                    print("Data : ", dic)
                    serializer = MegazinePagesSerializer(data=dic)
                    print(serializer)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save()            
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                return Response({'msg': 'Data Success Fully Saved.', 'data':serializer.data},status=status.HTTP_200_OK)

        except:
            if not check_serializer.is_valid():
                return Response(check_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            


#         return Response({'msg': 'Something Went Wrong.'}, status=status.HTTP_400_BAD_REQUEST)
        
        



