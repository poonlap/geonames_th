# geonames_th : โมดูลข้อมูลตำบล, อำเภอ, จังหวัด สำหรับ Odoo
โมดูลช่วยติดตั้งข้อมูลตำบล, อำเภอ, จังหวัด เป็นภาษาไทย (หรือภาษาอังกฤษ) โดยใช้โมดูล [Base Location Geonames Import](https://github.com/OCA/partner-contact/tree/13.0/base_location_geonames_import) ช่วย. เมื่อติดตั้งและ import ข้อมูลแล้ว จะสามารถค้นหาและเติมเต็ม (complement) ที่อยู่ได้ง่ายและถูกต้อง. ลดข้อผิดพลาดเช่น พิมพ์ชื่อตำบล, อำเภอ หรือจังหวัดผิด.

# วิธีติดตั้ง
- อ่าน[วิธีติดตั้งโมดูล](https://odoo-development.readthedocs.io/en/latest/odoo/usage/install-module.html)

โมดูลนี้รวมไว้ใน [docker odoo-th](https://hub.docker.com/r/poonlap/odoo-th) แล้ว สามารถลองใช้ได้ทันที.

# สาธิตการใช้งานจาก docker image
```bash
$ git clone https://github.com/poonlap/odoo-th.git
$ cd odoo-th/example
$ docker-compose up 
```
- ไปที่ `http://localhost:8069` 
- สร้าง database, username, password
- เมื่อ login แล้วไปที่ Apps

![](https://raw.githubusercontent.com/wiki/poonlap/odoo-th/images/geonames_th-install.png)

- ไปที่ Contacts > Configuration > Import from Geonames
- เลือกประเทศไทย แล้ว import

# วิธีใช้งาน
- สร้าง Contact หรือลูกค้าใหม่
- กรอกชื่อที่อยู่ตามปกติ พอจะกรอกตำบลหรือแขวง ให้ไปที่ช่อง "Location completion"

![](https://raw.githubusercontent.com/wiki/poonlap/odoo-th/images/geonames_th-input.png)

- กรอกค้นหา เช่น ชื่อตำบล หรือ ชื่ออำเภอ หรือ รหัสไปรษณีย์ แล้วเลือกข้อมูลที่ระบบหามาให้. แล้วระบบจะเติมช่อง street2 ให้เป็นตำบล, ช่อง city เป็นอำเภอ, ช่อง state เป็นจังหวัดให้อัตโนมัติ.

![](https://raw.githubusercontent.com/wiki/poonlap/odoo-th/images/geonames_th-completion.png)

# วีดีโอสาธิต
![](https://raw.githubusercontent.com/wiki/poonlap/odoo-th/images/geonames_th.gif)

[ดูที่ Youtube](https://youtu.be/0E1FfSh1ZsQ)

# โมดูลนี้จริงๆแล้วทำอะไร
- ติดตั้งโมดูล [Base Location Geonames Import](https://github.com/OCA/partner-contact/tree/13.0/base_location_geonames_import)
- ตั้งค่า system parameter `geonames.url` ไปที่

```
https://github.com/poonlap/odoo-th/raw/master/data/th/%s.zip
```

- เพิ่มภาษาไทยในระบบ (ยังไม่สามารถ load translation ต้องไปทำเอง)
- เปลี่ยน address_format ของ sales order ให้ใช้ชื่อจังหวัดจาก default เป็นรหัสจังหวัด (state code) แสดงผลตอนพิมพ์ (PDF)
- ดัดแปลงแก้ form ช่อง complement ให้เติมตำบลในช่อง street2 จากเดิมที่โมดูลเดิมไม่ได้เติมให้

โมดูลนี้เพิ่งเริ่มเขียน อาจจะไม่ถูกหลักการณ์. หากมีข้อแนะนำเชิญที่ [issue](https://github.com/poonlap/geonames_th/issues) ของโปรเจคนี้.
