# NPA2023-Final

ให้นักศึกษาเขียนโปรแกรมคล้ายกับที่กำหนดใน https://github.com/chotipat/NPA2023-Final-Example
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
2. หากที่ Router ยังไม่มี interface loopbackStudentID ให้ทำการสร้าง Interface loopbackStudentID ขึ้นมาก่อน หากมีอยู่แล้วไม่จำเป็นต้องสร้างอีก
3. ยกตัวอย่างเช่น หากนักศึกษามี studentID 66079999 เมื่อได้รับข้อความ "/66079999 create" ให้ทำการ สร้าง loopback interface 66079999 โดยมี IP address เป็น Private IP สุ่ม ในช่วง 172.30.xxx.yyy/24 แต่หากมี loopback interface 66079999 ใน Router อยู่แล้วก็ไม่จำเป็นต้องสร้างใหม่
4. เมื่อสร้าง interface loopback 66079999 แล้ว ให้ส่งข้อความ "Interface loopback 66079999 is created successfully" ไปที่ NPA2023 Webex Team room แต่ถ้ามี Interface loopback 66079999 อยู่แล้ว ก็ให้ส่งข้อความ "Cannot create: Interface loopback 66079999 is already existed"

## command = delete
1. เมื่อ command เป็น delete ให้นักศึกษาที่มี studentID ทำการ delete loopbackStudentID 
2. หากนักศึกษามี studentID 66079999 เมื่อได้รับข้อความ "/66079999 delete" ให้ตรวจสอบว่ามี interface loopback 66079999 หรือไม่ หากมีให้ทำการ delete loopback interface 66079999 และส่งข้อความ "Interface loopback 66079999 is deleted successfully" ไปที่ NPA2023 Webex Team room
3. แต่ถ้าที่ Router ยังไม่มี interface loopbackStudentID ให้ส่งข้อความ เช่น "Cannot delete: No interface loopback 66079999"

## command = enable
1. เมื่อ command เป็น enable ให้นักศึกษาที่มี studentID ทำการ enable หรือ no shutdown interface loopbackStudentID 
2. ยกตัวอย่างเช่น หากนักศึกษามี studentID 66079999 เมื่อได้รับข้อความ "/66079999 enable" ให้ทำการ enable หรือ no shutdown loopback interface 66079999 และส่งข้อความ "Interface loopback 66079999 is enabled successfully" ไปที่ NPA2023 Webex Team room
3. แต่หากยังไม่มี loopback interface 66079999 ใน Router ให้ส่งข้อความ "Cannot enable: no interface loopback 66079999"

## command = disable
1. เมื่อ command เป็น disable ให้นักศึกษาที่มี studentID ทำการ disable หรือ shutdown interface loopbackStudentID 
2. ยกตัวอย่างเช่น หากนักศึกษามี studentID 66079999 เมื่อได้รับข้อความ "/66079999 enable" ให้ทำการ disable หรือ shutdown loopback interface 66079999 และส่งข้อความ "Interface loopback 66079999 is shutdowned successfully" ไปที่ NPA2023 Webex Team room
3. แต่หากยังไม่มี loopback interface 66079999 ใน Router ให้ส่งข้อความ "Cannot shutdown: no interface loopback 66079999"

## command = status
1. เมื่อ command เป็น status ให้นักศึกษาที่มี studentID ทำการแสดงสถานะของ interface loopbackStudentID
2. ยกตัวอย่างเช่น หากนักศึกษามี studentID 66079999 เมื่อได้รับข้อความ "/66079999 status" ให้ส่งข้อความไปที่ NPA2023 Webex Team room ตามเงื่อนไขต่อไปนี้
- หากมี interface loopback 66079999 อยู่แล้ว และมีสถานะ up up ให้ส่งข้อความ "Interface loopback 66079999 is enabled"
- หากมี interface loopback 66079999 อยู่แล้ว และมีสถานะ down หรือ administratively shutdown" ให้ส่งข้อความ "Interface loopback 66079999 is disabled"
- หากไม่มี interface loopback 66079999 ให้ส่งข้อความ "No Interface loopback 66079999"
