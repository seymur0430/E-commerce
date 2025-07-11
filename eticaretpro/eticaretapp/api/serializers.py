from rest_framework import serializers
from eticaretapp.models import ( Banner, Product,  ProductContent, ProductPhoto, Review, Contanct,
    Store, Wishlist, Approval, SiteSettings 
)
from eticaretapp.models import CustomUser
from django.contrib.auth.password_validation import validate_password 



class UserCreateSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = CustomUser
        fields = ("username", "password")
        
        
    def validate(self, data):
        validate_password(data["password"])
        return data
    
    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        
        user = CustomUser.objects.create_user(
            username = username,
            password = password
        )
        return user
    
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ( 'image', 'name', 'price',)
    
    
class WishlistSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model= Wishlist
        fields= '__all__'
        
        
class WishlistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Wishlist
        fields= ("product",)
        
        
class ApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model= Approval
        fields= '__all__'
        
        
class ApprovalCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Approval
        fields= ('product')
        
        
class BannerSerializers(serializers.ModelSerializer):
    class Meta:
        model=Banner
        fields= '__all__'
        # exclude = ('id',)
        
        
class BannerRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Banner
        fields = "__all__"
        
        
        
class ProductRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Product
        fields = "__all__"        
        
        
        
class  ProductContentSerializer(serializers.ModelSerializer):
    class Meta:
        model =  ProductContent
        fields = ( 'image',)
        

class  ProductContentRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model  =  ProductContent
        fields = "__all__"
        
        
class  ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model =  ProductPhoto
        fields = ( 'image',)
        

class  ProductPhotoRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model  =  ProductPhoto
        fields = "__all__"
        
        
        
class  ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Review
        fields = ( 'image',)
        

class  ReviewRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model  =  Review
        fields = "__all__"
        
        
class  ContanctSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Contanct
        fields = ( 'image',)
        

class  ContanctRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model  =  Contanct
        fields = "__all__"
        
        
class  StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Store
        fields = ( 'image',)
        
       
class  SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model =  SiteSettings
        fields = ( 'image',)