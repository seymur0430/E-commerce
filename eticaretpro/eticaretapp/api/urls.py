from django.urls import path
from eticaretapp.api import views


urlpatterns = [
    path('user-create/', views.UserCreateAPIView.as_view()),
    path('banner-list/', views.BannerListAPIView.as_view()),
    path('banner-retrieve/<int:id>/', views.BannerRetrieveAPIView.as_view()),
   
    path('product-list/',views.ProductListAPIView.as_view()),
    path('product-retrieve/<int:id>/',views.ProductRetrieveAPIView.as_view()),
    
    path('productcontent-list/',views.ProductContentListAPIView.as_view()),
    path('productcontent-retrieve/<int:id>/',views.ProductContentRetrieveAPIView.as_view()),    
    path('productcontent-create/',views.ProductContentCreateAPIView.as_view()),
    path('productcontent-update/<int:id>/',views.ProductContentUpdateAPIView.as_view()),
    path('productcontent-delete/<int:id>/',views.ProductContentDestroyAPIView.as_view()),
    
    path('productphoto-list/',views.ProductPhotoListAPIView.as_view()),
    path('productphoto-retrieve/<int:id>/',views.ProductPhotoRetrieveAPIView.as_view()),
    path('productphoto-create/',views.ProductPhotoCreateAPIView.as_view()),
    path('productphoto-update/<int:id>/',views.ProductPhotoUpdateAPIView.as_view()),
    path('productphoto-delete/',views.ProductPhotoDestroyAPIView.as_view()),
    
    path('review-list/',views.ReviewListAPIView.as_view()),
    path('review-retrieve/<int:id>/',views.ReviewRetrieveAPIView.as_view()),                        
    path('review-create/',views.ReviewCreateAPIView.as_view()),
    path('review-update/<int:id>/',views.ReviewUpdateAPIView.as_view()),
    path('review-delete/<int:id>/',views.ReviewDestroyAPIView.as_view()),

    path('store-list/',views.StoreListAPIView.as_view()),
    path('contanct-list/', views.ContanctListAPIView.as_view()),
    path('sitesettings-list/', views.SiteSettingsListAPIView.as_view()),
    
    path('wishlist-list/', views.WishlistListAPIView.as_view()),  
    path('wishlist-create/',views.WishlistCreateAPIView.as_view()),
    path('user-wishlist-list/', views.UserWishlistListAPIView.as_view()),                  
    
    path('approval-list/', views.ApprovalListAPIView.as_view()),
    path('approval-create/',views.ApprovalCreateAPIView.as_view()),    
]