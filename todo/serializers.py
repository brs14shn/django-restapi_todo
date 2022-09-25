
from rest_framework import serializers

from .models import Todo,Category

from django.utils.timezone import now



#!Model Serializers


class TodoSerializers(serializers.ModelSerializer):
 
 
  days=serializers.SerializerMethodField()
  


  category=serializers.StringRelatedField()
  # 🍵 buradaki category todo modelindeki filed default id, biz __str__ methodundaki veriyi böylece çağırdık artık field category_name olarak gelir

  class Meta:
    model=Todo
    fields="__all__"
    # Eğer all olmasaydı days field içerisine eklemek gerekiyordu
  
  #* Object-level validation  
  """SerializerMethodField() methodu kullandık, bu method, modelden gelen tabloya serializers işlemi uygularken ek olarak veri eklemek için kullanılıyor"""

  def get_days(self,obj):
    return (now() - obj.createDate).days



  #* Field-level validation
  def validate_task(self,value):
    if value.lower() =="python":
        raise serializers.ValidationError("python can not be our task")

#! validate lere giriş adminden yapılan işlemler için kısıltlama getirmez
    
  




class CategorySerializers(serializers.ModelSerializer):

    #related name
    #categorys=TodoSerializers(many=True) # tüm todolar geldi

    #categorys=serializers.StringRelatedField(many=True) 
    # __str__ gelir
    categorys=serializers.PrimaryKeyRelatedField(many=True,read_only=True) # sadece Id

    class Meta:
        model=Category
        fields="__all__"