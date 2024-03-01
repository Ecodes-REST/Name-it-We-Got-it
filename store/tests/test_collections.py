from django.contrib.auth.models import User
from store.models import Collection
from store.models import Product
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APIClient
import pytest

@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/store/collections/',collection)
    return do_create_collection

@pytest.mark.django_db
class TestCreateCollection:
    def test_if_the_user_is_anonymous_returns_401(self, create_collection):
        response= create_collection({'title':'a'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_if_the_user_is_not_admin_returns_403(self, api_client, create_collection, authenticate):
        authenticate()
        response= create_collection({'title':'a'})

        assert response.status_code == status.HTTP_403_FORBIDDEN
    
    def test_if_the_user_if_data_is_invalid_returns_400(self, api_client, create_collection, authenticate):
        authenticate(is_staff= True)
        response= create_collection({'title':''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title']is not None
    
    def test_if_the_user_if_data_is_valid_returns_201(self, api_client, create_collection, authenticate):
        authenticate(is_staff= True)
        response= create_collection({'title':'a'})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id']>0

@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_collection_exists_returns_200(self, api_client):
        collection= baker.make(Collection)
        response= api_client.get(f'/store/collections/{collection.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id' : collection.id,
            'title' : collection.title,
            'products_count':0
        }

@pytest.mark.django_db
class TestListCollection:
    def test_if_collection_exists_returns_200(self, api_client):
        
        response= api_client.get(f'/store/collections/')

        assert response.status_code == status.HTTP_200_OK


@pytest.fixture
def full_update_collection(api_client):
    def do_full_update_collection(collection):
        collection= baker.make(Collection)
        return api_client.put(f'/store/collections/{collection.id}/')

    return do_full_update_collection

@pytest.mark.django_db
class TestUpdateCollection:
    def test_if_the_user_is_anonymous_returns_401(self, full_update_collection):
        response= full_update_collection({'title':'a'})
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED 
    
    def test_if_the_user_is_not_admin_returns_403(self, api_client, full_update_collection, authenticate):
        authenticate()
        response= full_update_collection({'title':'a'})

        assert response.status_code == status.HTTP_403_FORBIDDEN
    
    def test_if_the_user_if_data_is_invalid_returns_400(self, api_client, full_update_collection, authenticate):
        authenticate(is_staff= True)
        response= full_update_collection({'title':''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title']is not None
    
    def test_if_the_user_if_data_is_valid_returns_200(self, api_client, full_update_collection, authenticate):
        collection = baker.make(Collection)
        

        authenticate(is_staff= True)
        response= api_client.put(f'/store/collections/{collection.id}/', {'title': 'a'})

        assert response.status_code == status.HTTP_200_OK


@pytest.fixture
def partial_update_collection(api_client):
    def do_partial_update_collection(collection):
        collection= baker.make(Collection)
        return api_client.patch(f'/store/collections/{collection.id}/')

    return do_partial_update_collection

@pytest.mark.django_db
class TestUpdateCollection:
    def test_if_the_user_is_anonymous_returns_401(self, partial_update_collection):
        response= partial_update_collection({'title':'a'})
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED 
    
    def test_if_the_user_is_not_admin_returns_403(self, api_client, partial_update_collection, authenticate):
        authenticate()
        response= partial_update_collection({'title':'a'})

        assert response.status_code == status.HTTP_403_FORBIDDEN
    
    def test_if_the_user_if_data_is_invalid_returns_400(self, api_client, partial_update_collection, authenticate):
        collection = baker.make(Collection)
        authenticate(is_staff= True)
        response= api_client.patch(f'/store/collections/{collection.id}/', {'title': ''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title']is not None
    
    def test_if_the_user_if_data_is_valid_returns_200(self, api_client, partial_update_collection, authenticate):
        collection = baker.make(Collection)
        

        authenticate(is_staff= True)
        response= api_client.patch(f'/store/collections/{collection.id}/', {'title': 'a'})

        assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
class TestDestroyCollection:
    def test_if_collection_exists_returns_200(self, api_client, authenticate):
        collection= baker.make(Collection)
        authenticate(is_staff= True)
        response= api_client.delete(f'/store/collections/{collection.id}/')

        assert response.status_code == status.HTTP_204_NO_CONTENT
        



@pytest.fixture
def create_product(api_client):
    def do_create_product(product):
        return api_client.post('/store/products/', product)
    return do_create_product

@pytest.mark.django_db
class TestCreateProduct:
    def test_if_the_user_is_anonymous_returns_401(self, create_product):
        response= create_product({'title':'a'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_if_the_user_is_not_admin_returns_403(self, api_client, create_product, authenticate):
        authenticate()
        response= create_product({'title':'a'})

        assert response.status_code == status.HTTP_403_FORBIDDEN
    
    def test_if_the_user_if_data_is_invalid_returns_400(self, api_client, create_product, authenticate):
        authenticate(is_staff= True)
        response= create_product({'title':''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title']is not None
    
    def test_if_the_user_if_data_is_valid_returns_201(self, api_client, create_product, authenticate):
        authenticate(is_staff= True)
        response= create_product({'title':'a', 'slug':'-', 'inventory':'2','unit_price':'90','collection':'5'})

        print(response.status_code)
        print(response.data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id']>0
        
@pytest.mark.django_db
class TestRetrieveProduct:
    def test_if_product_exists_returns_200(self, api_client):
        product= baker.make(Product)
        response= api_client.get(f'/store/products/{product.id}/')

        assert response.status_code == status.HTTP_200_OK
        
@pytest.mark.django_db
class TestListProduct:
    def test_if_products_exists_returns_200(self, api_client):
        
        response= api_client.get(f'/store/products/')

        assert response.status_code == status.HTTP_200_OK


@pytest.fixture
def full_update_product(api_client):
    def do_full_update_product(collection):
        product= baker.make(Product)
        return api_client.put(f'/store/products/{product.id}/')

    return do_full_update_product

@pytest.mark.django_db
class TestUpdateProduct:
    def test_if_the_user_is_anonymous_returns_401(self, full_update_product):
        response= full_update_product({'title':'a'})
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED 
    
    def test_if_the_user_is_not_admin_returns_403(self, api_client, full_update_product, authenticate):
        authenticate()
        response= full_update_product({'title':'a'})

        assert response.status_code == status.HTTP_403_FORBIDDEN
    
    def test_if_the_user_if_data_is_invalid_returns_400(self, api_client, full_update_product, authenticate):
        authenticate(is_staff= True)
        response= full_update_product({'title':''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title']is not None
    
    def test_if_the_user_if_data_is_valid_returns_200(self, api_client, full_update_product, authenticate):
        product= baker.make(Product)
        

        authenticate(is_staff= True)
        response= api_client.put(f'/store/products/{product.id}/', {'title': 'a'})

        assert response.status_code == status.HTTP_200_OK


@pytest.fixture
def partial_update_product(api_client):
    def do_partial_update_product(collection):
        product= baker.make(Product)
        return api_client.patch(f'/store/products/{product.id}/')

    return do_partial_update_product

@pytest.mark.django_db
class TestUpdateProduct:
    def test_if_the_user_is_anonymous_returns_401(self, partial_update_product):
        response= partial_update_product({'title':'a'})
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED 
    
    def test_if_the_user_is_not_admin_returns_403(self, api_client, partial_update_product, authenticate):
        authenticate()
        response= partial_update_product({'title':'a'})

        assert response.status_code == status.HTTP_403_FORBIDDEN
    
    def test_if_the_user_if_data_is_invalid_returns_400(self, api_client, partial_update_product, authenticate):
        product = baker.make(Product)
        authenticate(is_staff= True)
        response= api_client.patch(f'/store/products/{product.id}/', {'title': ''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title']is not None
    
    def test_if_the_user_if_data_is_valid_returns_200(self, api_client, partial_update_product, authenticate):
        product = baker.make(Product)
        

        authenticate(is_staff= True)
        response= api_client.patch(f'/store/products/{product.id}/', {'title': 'a'})

        assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
class TestDestroyProduct:
    def test_if_product_exists_returns_200(self, api_client, authenticate):
        product= baker.make(Product)
        authenticate(is_staff= True)
        response= api_client.delete(f'/store/products/{product.id}/')

        assert response.status_code == status.HTTP_204_NO_CONTENT
        
