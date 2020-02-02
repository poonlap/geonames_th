# -*- coding: utf-8 -*-
{
    'name': "geonames_th",

    'summary': """
        A helper module for setting geonames in Thai.
        """,

    'description': """
    geonames\_th : โมดูลข้อมูลตำบล, อำเภอ, จังหวัด สำหรับ Odoo
==========================================================

โมดูลช่วยติดตั้งข้อมูลตำบล, อำเภอ, จังหวัด เป็นภาษาไทย (หรือภาษาอังกฤษ)
โดยใช้โมดูล `Base Location Geonames
Import <https://github.com/OCA/partner-contact/tree/13.0/base_location_geonames_import>`__
ช่วย. เมื่อติดตั้งและ import ข้อมูลแล้ว จะสามารถค้นหาและเติมเต็ม
(complement) ที่อยู่ได้ง่ายและถูกต้อง. ลดข้อผิดพลาดเช่น พิมพ์ชื่อตำบล,
อำเภอ หรือจังหวัดผิด.

วิธีติดตั้ง
===========

-  อ่าน\ `วิธีติดตั้งโมดูล <https://odoo-development.readthedocs.io/en/latest/odoo/usage/install-module.html>`__

โมดูลนี้รวมไว้ใน `docker
odoo-th <https://hub.docker.com/r/poonlap/odoo-th>`__ แล้ว
สามารถลองใช้ได้ทันที.

สาธิตการใช้งานจาก docker image
==============================

.. code:: bash

    $ git clone https://github.com/poonlap/odoo-th.git
    $ cd odoo-th/example
    $ docker-compose up 

-  ไปที่ ``http://localhost:8069``
-  สร้าง database, username, password
-  เมื่อ login แล้วไปที่ Apps

.. figure:: https://raw.githubusercontent.com/wiki/poonlap/odoo-th/images/geonames_th-install.png
   :alt: 

-  ไปที่ Contacts > Configuration > Import from Geonames
-  เลือกประเทศไทย แล้ว import

วิธีใช้งาน
==========

-  สร้าง Contact หรือลูกค้าใหม่
-  กรอกชื่อที่อยู่ตามปกติ พอจะกรอกตำบลหรือแขวง ให้ไปที่ช่อง "Location
   completion"

.. figure:: https://raw.githubusercontent.com/wiki/poonlap/odoo-th/images/geonames_th-input.png
   :alt: 

-  กรอกค้นหา เช่น ชื่อตำบล หรือ ชื่ออำเภอ หรือ รหัสไปรษณีย์
   แล้วเลือกข้อมูลที่ระบบหามาให้. แล้วระบบจะเติมช่อง street2
   ให้เป็นตำบล, ช่อง city เป็นอำเภอ, ช่อง state เป็นจังหวัดให้อัตโนมัติ.

.. figure:: https://raw.githubusercontent.com/wiki/poonlap/odoo-th/images/geonames_th-completion.png
   :alt: 

วีดีโอสาธิต
===========

.. figure:: https://raw.githubusercontent.com/wiki/poonlap/odoo-th/images/geonames_th-completion.png
   :alt: 

`ดูที่ Youtube <https://youtu.be/0E1FfSh1ZsQ>`__

โมดูลนี้จริงๆแล้วทำอะไร
=======================

-  ติดตั้งโมดูล `Base Location Geonames
   Import <https://github.com/OCA/partner-contact/tree/13.0/base_location_geonames_import>`__
-  ตั้งค่า system parameter ``geonames.url`` ไปที่

::

    https://github.com/poonlap/odoo-th/raw/master/data/th/%s.zip

-  เพิ่มภาษาไทยในระบบ (ยังไม่สามารถ load translation ต้องไปทำเอง)
-  เปลี่ยน address\_format ของ sales order ให้ใช้ชื่อจังหวัดจาก default
   เป็นรหัสจังหวัด (state code) แสดงผลตอนพิมพ์ (PDF)
-  ดัดแปลงแก้ form ช่อง complement ให้เติมตำบลในช่อง street2
   จากเดิมที่โมดูลเดิมไม่ได้เติมให้

โมดูลนี้เพิ่งเริ่มเขียน อาจจะไม่ถูกหลักการณ์. หากมีข้อแนะนำเชิญที่
`issue <https://github.com/poonlap/geonames_th/issues>`__ ของโปรเจคนี้.

    """,

    'author': "Poonlap V.",
    'website': "https://github.com/poonlap/geonames_th",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Localization',
    'version': '13.0.1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base_location_geonames_import'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
        'views/view_config_parameter.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
