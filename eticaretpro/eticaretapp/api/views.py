from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView 
from eticaretapp.models import Banner, Product,  ProductContent, ProductPhoto, Review, Contanct, Store, SiteSettings
from eticaretapp.models import CustomUser
from eticaretapp.models import Wishlist
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from eticaretapp.models import Approval

from eticaretapp.api.serializers import ( BannerSerializers , BannerRetrieveSerializer, 
    ProductSerializer, ProductContentSerializer, ProductRetrieveSerializer,  ProductPhotoSerializer, ReviewSerializer,
    ContanctSerializer, StoreSerializer,  SiteSettingsSerializer,
    WishlistSerializer, ApprovalSerializer, WishlistCreateSerializer, UserCreateSerializers, 
)



class UserCreateAPIView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializers
    
    
class WishlistListAPIView(ListAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAdminUser]
    
    
    
class UserWishlistListAPIView(ListAPIView):
    def get_queryset(self):
         return Wishlist.objects.filter(
             user = self.request.user
         )
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]

  
class WishlistCreateAPIView(CreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistCreateSerializer
    permission_classes = (IsAuthenticated,)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer .errors, status=status.HTTP_400_BAD_REQUEST) 
    
  
class ApprovalListAPIView(ListAPIView):
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializer
    permission_classes = (IsAdminUser,)
    
    
class UserApprovalListAPIView(ListAPIView):
    def get_queryset(self):
         return Approval.objects.filter(
             user = self.request.user
         )
    serializer_class = ApprovalSerializer
    
    
class ApprovalCreateAPIView(CreateAPIView):
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializer
    permission_classes = (IsAuthenticated,)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer .errors, status=status.HTTP_400_BAD_REQUEST)  
    


class BannerListAPIView(ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializers
    
    
class BannerRetrieveAPIView(RetrieveUpdateAPIView):
    queryset = Banner.objects.all()
    serializer_class =BannerRetrieveSerializer
    lookup_field = "id"
    

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductRetrieveSerializer
    lookup_field = "id"
    
    
class ProductContentListAPIView(ListAPIView):
    queryset = ProductContent.objects.all()
    serializer_class = ProductContentSerializer
    
class ProductContentRetrieveAPIView(RetrieveAPIView):
    queryset = ProductContent.objects.all()
    serializer_class = ProductContentSerializer
    lookup_field = "id"
    
class ProductContentCreateAPIView(CreateAPIView):
    queryset = ProductContent.objects.all()
    serializer_class = ProductContentSerializer
    
class ProductContentUpdateAPIView(UpdateAPIView):
    queryset = ProductContent.objects.all()
    serializer_class = ProductContentSerializer
    lookup_field = "id"
    
class ProductContentDestroyAPIView(DestroyAPIView):
    queryset = ProductContent.objects.all()
    serializer_class = ProductContentSerializer
    lookup_field = "id"
    
    
class  ProductPhotoListAPIView(ListAPIView):
    queryset =  ProductPhoto.objects.all()
    serializer_class =  ProductPhotoSerializer
    
class  ProductPhotoRetrieveAPIView(RetrieveAPIView):
    queryset =  ProductPhoto.objects.all()
    serializer_class =  ProductPhotoSerializer
    lookup_field = "id"
    
class  ProductPhotoCreateAPIView(CreateAPIView):
    queryset = ProductPhoto.objects.all()
    serializer_class =  ProductPhotoSerializer
    
class  ProductPhotoUpdateAPIView(UpdateAPIView):
    queryset =  ProductPhoto.objects.all()
    serializer_class =  ProductPhotoSerializer
    lookup_field = "id"
    
class  ProductPhotoDestroyAPIView(DestroyAPIView):
    queryset =  ProductPhoto.objects.all()
    serializer_class =  ProductPhotoSerializer
    
    
class ReviewListAPIView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
class ReviewRetrieveAPIView(RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = "id"
    
class ReviewCreateAPIView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    
class ReviewUpdateAPIView(UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
class ReviewDestroyAPIView(DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = "id"
    
    
class ContanctListAPIView(ListAPIView):
    queryset = Contanct.objects.all()
    serializer_class = ContanctSerializer
    
    
class StoreListAPIView(ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class SiteSettingsListAPIView(ListAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer
    