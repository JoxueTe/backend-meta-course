from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from .models import MenuItem, Category
from .serializers import MenuItemSerializer, CategorySerializer
from django.core.paginator import Paginator, EmptyPage

#Menu Items
@api_view(['GET','POST'])
def menu_items(request):
    if(request.method == 'GET'):
        items = MenuItem.objects.select_related('category').all() #query items from models
        category_name = request.query_params.get('category') #asigne category receive on the request
        to_price = request.query_params.get('to_price') # get price value receive on the reques if any
        search = request.query_params.get('search')# get search value receive on the reques if any
        ordering = request.query_params.get('ordering')
        perpage = request.query_params.get('perpage', default=2)
        page = request.query_params.get('page', default=1)

        # if category, price, search are foun don the request, filter response
        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price__lte=to_price) #lte stands less than or equal to
        if search:
            items = items.filter(title__icontains=search)
        if ordering:
            ordering_fields = ordering.split(",")
            items = items.order_by(*ordering_fields)

        #Paginate results
        paginator = Paginator(items, per_page=perpage)
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items = []

        #Return serialize data
        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)
    elif request.method == 'POST':
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.validated_data, status.HTTP_201_CREATED)
    
@api_view
def single_item(request, id):
    item = get_object_or_404(MenuItem,pk=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)

#Categories
@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category,pk=pk)
    serialized_category = CategorySerializer(category)
    return Response(serialized_category.data) 

@api_view() 
@renderer_classes ([TemplateHTMLRenderer])
def menu(request):
    items = MenuItem.objects.select_related('category').all()
    serialized_item = MenuItemSerializer(items, many=True)
    return Response({'data':serialized_item.data}, template_name='menu-items.html')


#Menu Items with class base view
# class MenuItemsView(generics.ListCreateAPIView):
#     queryset = MenuItem.objects.select_related('category').all()
#     serializer_class = MenuItemSerializer
#     ordering_fields=['price','inventory']
#     search_fields=['title','category__title']

# class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView, generics.DestroyAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer

# @api_view(['GET','POST'])
# def books(request):
#     return Response('list of the books', status=status.HTTP_200_OK)

# class BookList(APIView):
#     def get(self, request):
#         author = request.GET.get('author')
#         if(author):
#             return Response({"message":"list of the books by " + author}, status.HTTP_200_OK)
        
#         return Response({"message":"list of the books"}, status.HTTP_200_OK)

#     def post(self, request):
#         return Response({"title":request.data.get('title')}, status.HTTP_201_CREATED)
    
# class Book(APIView):
#     def get(self, request, pk):
#         return Response({"message":"single book with id " + str(pk)}, status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         return Response({"title":request.data.get('title')}, status.HTTP_200_OK)
