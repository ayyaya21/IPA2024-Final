# IPA2024-Final

## Instruction

1. Fork repository นี้ไปยัง GitHub repository ของตนเอง
2. ทำการ Clone repository จาก GitHub repository ของตนเอง ไปยัง GitHub/local repository ในเครื่องของตนเอง
3. ดำเนินการเขียนโปรแกรมตามดังรูปแบบที่เคยทำใน <https://github.com/chotipat/NPA2023-Final> 
4. ให้ commit และเขียน commit message ที่ดี อยู่เป็นระยะ
5. เมื่อทำเสร็จแล้ว ให้ส่งข้อมูลชื่อ นามสกุล GitHub URL และตอบคำถามลงใน Google Form ที่ <https://forms.gle/4oRJYJuUgnVTNFgh7> ภายในเวลา 15:30 น.

มีโจทย์ 2 ข้อ

## โจทย์ข้อ 1 (10 คะแนน) คล้ายกับ โจทย์ข้อสอบ NPA2023 Final มีเปลี่ยนแปลงเล็กน้อย ให้นักศึกษาทำโจทย์ข้อ 1 ให้เสร็จก่อน จึงทำโจทย์ข้อ 2 

เมื่อได้รับข้อความ "/studentID command" ให้นักศึกษาที่มี studentID ตรงกับค่าในข้อความทำการตาม command ที่ระบุในข้อความ โดย command มีได้ 5 แบบ ได้แก่

1. create
2. delete
3. enable
4. disable
5. status

สำหรับโจทย์ข้อ 1 ให้นักศึกษาดำเนินการตาม command ที่ Router IP 10.0.15.199 โดยใช้ Netconf หรือ Restconf (ให้เลือกใช้อย่างใดอย่างหนึ่ง หากต้องการใช้ NETCONF ก็ให้ไปเขียนโปรแกรมเพิ่มที่ netconf_final.py หากต้องการใช้ RESTCONF ก็ให้ edit ที่ restconf_final.py)

ไฟล์โปรแกรมหลักจะอยู่ที่ npa2024_final.py หากต้องการใช้ Netconf ก็ให้ import netconf_final ลงไปใน npa2024_final.py แต่หากต้องการใช้ Restconf ให้ import restconf_final ลงไปใน npa2024_final.py

Router IP 10.0.15.199 ได้ enable Netconf และ Restconf พร้อมใช้งานแล้ว สามารถเข้าถึงได้ด้วย username admin password cisco จากเครือข่ายภายในคณะฯ

### command = create

1. เมื่อ command เป็น create ให้นักศึกษาที่มี studentID ทำการสร้าง interface loopbackStudentID
2. หากที่ Router ยังไม่มี interface loopbackStudentID ให้ทำการสร้าง Interface loopbackStudentID ขึ้นมา หากมีอยู่แล้วไม่จำเป็นต้องสร้างอีก
3. ยกตัวอย่างเช่น หากนักศึกษามี studentID 66070123 เมื่อได้รับข้อความ "/66070123 create" ให้ทำการ สร้าง loopback interface 66070123 โดยมี IP address เป็น Private IP 172.30.xxx.1/24 (ในที่นี้ xxx = 123 เนื่องจากเป็นเลข 3 หลักสุดท้ายของ studentID) แต่หากมี loopback interface 66070123 ใน Router อยู่แล้วก็ไม่จำเป็นต้องสร้างใหม่
4. เมื่อสร้าง interface loopback 66070123 แล้ว ให้ส่งข้อความ "Interface loopback 66070123 is created successfully" ไปที่ NPA2024 Webex Team room แต่ถ้ามี Interface loopback 66070123 อยู่แล้ว ก็ให้ส่งข้อความ "Cannot create: Interface loopback 66070123"

### command = delete

1. เมื่อ command เป็น delete ให้นักศึกษาที่มี studentID ทำการ delete loopbackStudentID
2. หากนักศึกษามี studentID 66070123 เมื่อได้รับข้อความ "/66070123 delete" ให้ตรวจสอบว่ามี interface loopback 66070123 หรือไม่ หากมีให้ทำการ delete loopback interface 66070123 และส่งข้อความ "Interface loopback 66070123 is deleted successfully" ไปที่ NPA2024 Webex Team room
3. แต่ถ้าที่ Router ยังไม่มี interface loopbackStudentID ให้ส่งข้อความ เช่น "Cannot delete: Interface loopback 66070123"

### command = enable

1. เมื่อ command เป็น enable ให้นักศึกษาที่มี studentID ทำการ enable หรือ no shutdown interface loopbackStudentID
2. ยกตัวอย่างเช่น หากนักศึกษามี studentID 66070123 เมื่อได้รับข้อความ "/66070123 enable" ให้ทำการ enable หรือ no shutdown loopback interface 66070123 และส่งข้อความ "Interface loopback 66070123 is enabled successfully" ไปที่ NPA2024 Webex Team room
3. แต่หากยังไม่มี loopback interface 66070123 ใน Router ให้ส่งข้อความ "Cannot enable: Interface loopback 66070123"

### command = disable

1. เมื่อ command เป็น disable ให้นักศึกษาที่มี studentID ทำการ disable หรือ shutdown interface loopbackStudentID
2. ยกตัวอย่างเช่น หากนักศึกษามี studentID 66070123 เมื่อได้รับข้อความ "/66070123 disable" ให้ทำการ disable หรือ shutdown loopback interface 66070123 และส่งข้อความ "Interface loopback 66070123 is shutdowned successfully" ไปที่ NPA2024 Webex Team room
3. แต่หากยังไม่มี loopback interface 66070123 ใน Router ให้ส่งข้อความ "Cannot shutdown: Interface loopback 66070123"

### command = status

1. เมื่อ command เป็น status ให้นักศึกษาที่มี studentID ทำการแสดงสถานะของ interface loopbackStudentID
2. ยกตัวอย่างเช่น หากนักศึกษามี studentID 66070123 เมื่อได้รับข้อความ "/66070123 status" ให้ส่งข้อความไปที่ NPA2024 Webex Team room ตามเงื่อนไขต่อไปนี้

- หากมี interface loopback 66070123 อยู่แล้ว และมีสถานะ up ให้ส่งข้อความ "Interface loopback 66070123 is enabled"
- หากมี interface loopback 66070123 อยู่แล้ว และมีสถานะ (admin-status และ oper-status) down ให้ส่งข้อความ "Interface loopback 66070123 is disabled"
- หากไม่มี interface loopback 66070123 ให้ส่งข้อความ "No Interface loopback 66070123"

## Hint

นักศึกษาสามารถศึกษาตัวอย่าง RESTCONF API ได้โดยการ import collection URL นี้ ลงในโปรแกรม Postman
<https://elements.getpostman.com/redirect?entityId=4426393-69dd44cf-c218-46a4-a787-a98c88ca999a&entityType=collection>

และศึกษาตัวอย่างเพิ่มเติมของ NETCONF และ RESTCONF ได้ที่
<https://github.com/chotipat/NPA2023>

Router ใช้ IOS XE 16.9.5 ดังนั้นศึกษา Yang model ได้ที่ <https://github.com/YangModels/yang/tree/main/vendor/cisco/xe/1693>

หลักๆ สามารถใช้ ietf-interfaces.yang ในการทำโจทย์ข้อนี้ <https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1693/ietf-interfaces.yang>

ใช้ <https://codebeautify.org/xmlviewer> เพื่อดู xml
ใช้ <https://codebeautify.org/jsonviewer> เพื่อดู json

# โจทย์ ข้อ 2 (10 คะแนน) ให้รับ command เพิ่มอีก 2 command โดยใช้ Netmiko และ Ansible 

เมื่อได้รับข้อความ "/studentID command" ให้นักศึกษาที่มี studentID ตรงกับค่าในข้อความทำการตาม command ที่ระบุในข้อความ โดย command มีได้เพิ่มอีก 2 แบบ ได้แก่

1. gigabit_up_down
2. backup

### command = gigabit_up_down

ให้นักศึกษาดำเนินการตาม command gigabit_up_down ที่ Router IP 10.0.15.199 โดยใช้ Netmiko/TextFSM ไปเขียนโปรแกรมเพิ่มที่ netmiko_final.py เพื่อดูว่ามี Interface GigtabitEthernet ใดบ้างที่ Up อยู่ เช่น หาก Interface GigabitEthernet1-3 up แต่ GigabitEthernet4 down อยู่ ให้แสดงข้อความด้านล่างกลับไปที่ IPA2024 Webex Team room

GigabitEthernet 1 up, GigabitEthernet 2 up, GigabitEthernet 3 up, GigabitEthernet 4 down -> 3 up 1 down

- ห้าม Shutdown GigatbitEthernet1 เนื่องจากว่าเป็น Interface ที่ต่อกับ Cloud และมี IP 10.0.15.199 หาก Shutdown interface นี้จะทำให้ไม่สามารถติดต่อกับ Router ได้
- สามารถ console เข้ามา shutdown/no shutdown GigabitEthernet2-4 ได้ แต่ต้องระวังว่าทุกคน share Router เดียวกันอยู่

### command = ipv6

ให้นักศึกษาแก้ไข ansible playbook ที่เคยทำ Lab ใน Part 4 Use Ansible to Configure a Device ของ Lab - Use Ansible to Back Up and Configure a Device
https://docs.google.com/document/d/1Mdrh0y8u0Dcf9-AC9cnCATlVcuC5ZyIm/edit?usp=drive_link&ouid=109883484669217093529&rtpof=true&sd=true เพื่อตั้งค่า IPv6 address ของ Loopback Interface ของนักศึกษาที่ทำมาในโจทย์ข้อ 1 

และให้นักศึกษาเขียนโปรแกรมใน ansible_final.py เพื่อเรียก Ansible playbook ให้ทำงาน จากนั้นให้อ่านข้อความ IPv6_output_CSR1kv.txt จากเครื่องของนักศึกษา และส่งข้อความนั้นมาที่ IPA2024 Webex Team room
ทดลองเปลี่ยน IPv6 เพื่อทดสอบว่าโปรแกรมสามารถทำงานได้ปกติหรือไม่

ให้ commit ไฟล์ที่เกี่ยวข้องกับ ansible ทั้งหมด เช่น host file, playbook.yaml file, IPv6_output_CSR1kv.txt file ด้วย



