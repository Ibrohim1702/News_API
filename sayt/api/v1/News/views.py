from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
from api.v1.News.serialazer import NewsSerializer
from api.v1.News.services import paginated_news, format_news
# from base.helper import BearerToken
from sayt_api.models import News


class NewsView(GenericAPIView):
    serializer_class = NewsSerializer
    # permission_classes = (IsAuthenticated,)
    # # authentication_classes = (BearerToken,)

    def get_object(self, pk=None):
        try:
            root = News.objects.get(pk=pk)
        except:
            raise NotFound(f"{pk} IDsidagi categoriya yo'q!")
        return root

    def delete(self, requests, pk, *args, **kwargs):
        print("asdfasd")
        ctg = News.objects.filter(pk=pk).first()
        if not ctg:
            result = {"ErrOr": "Bunday category mavjud emas!"}

        else:
            ctg.delete()
            result = {"Success": "Category o'chirib tashlandi!"}

        return Response(result)

    def get(self, requests, pk=None, *args, **kwargs):
        if pk:
            ctg = News.objects.filter(pk=pk).first()
            if not ctg:
                result = {"ERROR": "Bunday categoriya mavjud emas!"}
            else:
                result = format_news(ctg)
        else:
            result = paginated_news(requests)

        return Response(result)

    def post(self, requests, *args, **kwargs):
        data = requests.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        result = serializer.create(serializer.data)

        return Response(format_news(result))

    def put(self, requests, pk, *args, **kwargs):
        root = self.get_object(pk)
        data = requests.data
        serializer = self.serializer_class(data=data, instance=root, partial=True)
        serializer.is_valid(raise_exception=True)
        if "image1" in requests.data:
            serializer.image1 = requests.data.get('image1')
        if "image2" in requests.data:
            serializer.image2 = requests.data.get('image2')
        data = serializer.save()

        return Response(format_news(data))
