# NPA2023-Final

ให้นักศึกษาเขียนโปรแกรมในรูปแบบที่กำหนดใน <https://github.com/chotipat/NPA2023-Final-Example>
โดยมีการเปลี่ยนแปลงดังนี้

เมื่อได้รับข้อความ "/studentID command" ให้นักศึกษาที่มี studentID ตรงกับค่าในข้อความทำการตาม command ที่ระบุในข้อความ โดย command มีได้ 5 แบบ ได้แก่

1. create
2. delete
3. enable
4. disable
5. status

ให้นักศึกษาดำเนินการตาม command ที่ Router IP 10.0.15.189 โดยใช้ Netconf หรือ Restconf (Router นี้มีการ enable Netconf และ Restconf พร้อมใช้งานแล้ว)

## command = create

1. เมื่อ command เป็น create ให้นักศึกษาที่มี studentID ทำการสร้าง interface loopbackStudentID
2. หากที่ Router ยังไม่มี interface loopbackStudentID ให้ทำการสร้าง Interface loopbackStudentID ขึ้นมา หากมีอยู่แล้วไม่จำเป็นต้องสร้างอีก
3. ยกตัวอย่างเช่น หากนักศึกษามี studentID 66070123 เมื่อได้รับข้อความ "/66070123 create" ให้ทำการ สร้าง loopback interface 66070123 โดยมี IP address เป็น Private IP 172.30.xxx.1/24 (ในที่นี้ xxx = 123 เนื่องจากเป็นเลข 3 หลักสุดท้ายของ studentID) แต่หากมี loopback interface 66070123 ใน Router อยู่แล้วก็ไม่จำเป็นต้องสร้างใหม่
4. เมื่อสร้าง interface loopback 66070123 แล้ว ให้ส่งข้อความ "Interface loopback 66070123 is created successfully" ไปที่ NPA2023 Webex Team room แต่ถ้ามี Interface loopback 66070123 อยู่แล้ว ก็ให้ส่งข้อความ "Cannot create: Interface loopback 66070123"

## command = delete

1. เมื่อ command เป็น delete ให้นักศึกษาที่มี studentID ทำการ delete loopbackStudentID
2. หากนักศึกษามี studentID 66070123 เมื่อได้รับข้อความ "/66070123 delete" ให้ตรวจสอบว่ามี interface loopback 66070123 หรือไม่ หากมีให้ทำการ delete loopback interface 66070123 และส่งข้อความ "Interface loopback 66070123 is deleted successfully" ไปที่ NPA2023 Webex Team room
3. แต่ถ้าที่ Router ยังไม่มี interface loopbackStudentID ให้ส่งข้อความ เช่น "Cannot delete: Interface loopback 66070123"

## command = enable

1. เมื่อ command เป็น enable ให้นักศึกษาที่มี studentID ทำการ enable หรือ no shutdown interface loopbackStudentID
2. ยกตัวอย่างเช่น หากนักศึกษามี studentID 66070123 เมื่อได้รับข้อความ "/66070123 disable" ให้ทำการ enable หรือ no shutdown loopback interface 66070123 และส่งข้อความ "Interface loopback 66070123 is enabled successfully" ไปที่ NPA2023 Webex Team room
3. แต่หากยังไม่มี loopback interface 66070123 ใน Router ให้ส่งข้อความ "Cannot enable: Interface loopback 66070123"

## command = disable

1. เมื่อ command เป็น disable ให้นักศึกษาที่มี studentID ทำการ disable หรือ shutdown interface loopbackStudentID
2. ยกตัวอย่างเช่น หากนักศึกษามี studentID 66070123 เมื่อได้รับข้อความ "/66070123 enable" ให้ทำการ disable หรือ shutdown loopback interface 66070123 และส่งข้อความ "Interface loopback 66070123 is shutdowned successfully" ไปที่ NPA2023 Webex Team room
3. แต่หากยังไม่มี loopback interface 66070123 ใน Router ให้ส่งข้อความ "Cannot shutdown: Interface loopback 66070123"

## command = status

1. เมื่อ command เป็น status ให้นักศึกษาที่มี studentID ทำการแสดงสถานะของ interface loopbackStudentID
2. ยกตัวอย่างเช่น หากนักศึกษามี studentID 66070123 เมื่อได้รับข้อความ "/66070123 status" ให้ส่งข้อความไปที่ NPA2023 Webex Team room ตามเงื่อนไขต่อไปนี้

- หากมี interface loopback 66070123 อยู่แล้ว และมีสถานะ up ให้ส่งข้อความ "Interface loopback 66070123 is enabled"
- หากมี interface loopback 66070123 อยู่แล้ว และมีสถานะ (admin-status และ oper-status) down ให้ส่งข้อความ "Interface loopback 66070123 is disabled"
- หากไม่มี interface loopback 66070123 ให้ส่งข้อความ "No Interface loopback 66070123"

นักศึกษาสามารถศึกษาตัวอย่าง RESTCONF API ได้โดยการ import collection URL นี้ ลงในโปรแกรม Postman
<https://api.postman.com/collections/4426393-69dd44cf-c218-46a4-a787-a98c88ca999a?access_key=PMAT-01HPR144H4Z5X2AXGWQBG9YC41>

และศึกษาตัวอย่างเพิ่มเติมได้ที่
<https://github.com/chotipat/NPA2023/tree/main/restconf>
