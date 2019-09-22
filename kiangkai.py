#!/usr/bin/env python
# coding: utf-8

# # 1 Month

# In[2]:


month=["Jan","May","Jul","Aug","Oct","Dec"]
month.insert(1,"Feb")
month.insert(2,"Mar")
month.insert(3,"Apr")
month.insert(5,"Jun")
month.insert(8,"Sep")
month.insert(10,"Nov")
print("แทรกเดือนที่ขาดหายไป =",month)
month.remove("Feb")
month.remove("May")
month.remove("Sep")
print("ลบชื่อเดือนตำแหน่งที่ 2,5,9 ออกจากลิสต์ =",month)
print("แสดงชื่อเดือนที่เหลืออยู่ในลิสต์ =",month)


# # 2Day

# In[4]:


day = ["Sun","Mon","Tuel","Wed","Thu","Fri","Sat"]
day.reverse()
print("เรียงชื่อวันจากท้ายสุด =",day)
day.sort()
print("เรียงลำดับชื่อวันตามตัวอักษร =",day)
print("แสดงชื่อวันในตำแหน่งที่ 3,5 และ 7 =",day[2:7:2])


# In[ ]:




