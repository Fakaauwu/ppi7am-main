package Controllers;


import Models.ProductModel;
import Services.ProductServices;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;

@CrossOrigin
@RestController
@RequestMapping("/products")
public class ProductController {
    @Autowired
    ProductServices productService;

    //GET
    @GetMapping()
    public ArrayList<ProductModel> findAllProducts(){
        return productService.findallproducts();
    }

    //POST

    @PostMapping()
    public ProductModel saveProduct(@RequestBody ProductModel product){
        return productService.saveProduct(product);

    }
}
