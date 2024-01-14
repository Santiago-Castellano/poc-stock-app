from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=1_000)
    link = models.CharField(max_length=10_000, null=True, blank=True)
    price = models.IntegerField()
    total_uses = models.IntegerField()

    def __str__(self):
        return self.name
    
    @property
    def price_per_use(self):
        return self.price / self.total_uses


class Service(models.Model):
    name = models.CharField(max_length=1_000)
    earn = models.IntegerField()


    def __str__(self):
        return self.name


    @property
    def cost(self):
        services_product = self.products.all().select_related("product")
        return int(sum([service_product.uses * service_product.product.price_per_use for service_product in services_product]))
    
    @property
    def price(self):
        return int(self.cost * (1 + (self.earn / 100)))


class ServiceProduct(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="products")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="uses_in_services")
    uses = models.IntegerField()

    def __str__(self):
        return f"{self.service} - {self.product} - USOS: {self.uses}"