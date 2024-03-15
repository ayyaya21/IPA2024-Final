# NPA2023-Final

ให้นักศึกษาเขียนโปรแกรมคล้ายกับที่กำหนดใน https://github.com/chotipat/NPA2023-Final-Example
โดยมีการเปลี่ยนแปลงดังนี้

เมื่อได้รับข้อความ "/studentID command" ให้นักศึกษาที่มี studentID ตรงกับค่าในข้อความทำการตาม command ที่ระบุในข้อความ โดย command มีได้ 3 แบบ ได้แก่ enable หรือ disable หรือ status เท่านั้น

## command = enable
1. เมื่อ command เป็น enable ให้นักศึกษาที่มี studentID ทำการ enable หรือ no shutdown interface loopbackStudentID ที่ Router ที่มี IP 10.0.15.189 โดยใช้ Netconf หรือ Restconf
2. หากที่ Router ยังไม่มี interface loopbackStudentID ให้ทำการสร้าง Interface loopbackStudentID ขึ้นมาก่อน
3. ยกตัวอย่างเช่น หากนักศึกษามี studentID 66079999 เมื่อได้รับข้อความ "/66079999 enable" ให้ทำการ enable หรือ no shutdown loopback interface 66079999 แต่หากยังไม่มี loopback interface 66079999 ใน Router ให้ทำการสร้าง interface loopback interface 66079999 ขึ้นมาก่อน โดยให้ทำทั้งหมดนี้ด้วย Netconf หรือ Restconf ก็ได้
4. เมื่อดำเนินการข้างต้นเรียบร้อยแล้ว ให้แจ้งว่า "Interface loopback 66079999 is enabled successfully." หากไม่สำเร็จให้แจ้งข้อความว่าไม่สำเร็จ (ให้กำหนดข้อความเอง)

## command = disable
6. เมื่อ command เป็น disable ให้นักศึกษาที่มี studentID ทำการ disable หรือ shutdown interface loopbackStudentID ที่ Router ที่มี IP 10.0.15.189 โดยใช้ Netconf หรือ Restconf
3. หากที่ Router ยังไม่มี interface loopbackStudentID ให้แจ้งว่า "No interface loopback 66
4. ยกตัวอย่างเช่น หากนักศึกษามี studentID 66079999 เมื่อได้รับข้อความ "/66079999 enable" ให้ทำการ enable หรือ no shutdown loopback interface 66079999 แต่หากยังไม่มี loopback interface 66079999 ใน Router ให้ทำการสร้าง interface loopback interface 66079999 ขึ้นมาก่อน โดยให้ทำทั้งหมดนี้ด้วย Netconf หรือ Restconf ก็ได้
