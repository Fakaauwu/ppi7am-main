package Services;

import Models.ProductModel;
import Repositories.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;

@Service
public class ProductServices {
    @Autowired
    ProductRepository productRepository;


    //obtener productos

    public ArrayList<ProductModel> findallproducts(){
        return (ArrayList<ProductModel>) productRepository.findAll();
    }

    //guardar un producto


    public ProductModel saveProduct(ProductModel product){
        return productRepository.save(product);
    }

}
