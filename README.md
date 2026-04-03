# DigiRank SEO Agency

> บริษัทรับทำ SEO ครบวงจร - พัฒนาด้วย Django Framework
> รายวิชา ICT12367 การใช้กรอบงานสำหรับการพัฒนาเว็บแอปพลิเคชันเพื่อความมั่นคงปลอดภัย
> มหาวิทยาลัยศรีปทุม (SPU)

## ผู้พัฒนา

- **ชื่อ:** ชินภัทร บุญยศ
- **รหัสนักศึกษา:** 68103144
- **คณะ:** เทคโนโลยีสารสนเทศ (SIT)

---

## เกี่ยวกับโปรเจค

เว็บไซต์ **DigiRank SEO** เป็นระบบจัดการลูกค้า SEO (CRM) สำหรับบริษัทรับทำ SEO ครบวงจร พัฒนาด้วย Django Framework ตามโมเดล MVT (Model-View-Template) พร้อมระบบ CRUD ครบถ้วน

## ฟีเจอร์หลัก

- **หน้าแรก (Landing Page)** - แสดงข้อมูลบริษัท, สถิติ, บริการ, ลูกค้าล่าสุด
- **หน้าบริการ** - แสดงบริการ SEO 6 ประเภท พร้อมแพ็คเกจราคา 4 ระดับ
- **ระบบจัดการลูกค้า (CRUD)**
  - เพิ่มข้อมูลลูกค้าใหม่
  - แสดงข้อมูลลูกค้าทั้งหมดในตาราง
  - แก้ไขข้อมูลลูกค้า
  - ลบข้อมูลลูกค้า (มี Modal แจ้งเตือนยืนยันก่อนลบ)
- **ค้นหาข้อมูล** - ค้นหาด้วย 3 เงื่อนไข (ชื่อบริษัท/เว็บไซต์, แพ็คเกจ, สถานะ)
- **หน้าเกี่ยวกับเรา** - ข้อมูลบริษัท, ค่านิยม, ทีมงาน
- **หน้าติดต่อ** - ข้อมูลติดต่อ, ฟอร์มส่งข้อความ, แผนที่

## เทคโนโลยีที่ใช้

| เทคโนโลยี | รายละเอียด |
|---|---|
| **Backend** | Django 5.x (Python) |
| **Frontend** | Bootstrap 5.3, Bootstrap Icons |
| **Database** | SQLite3 |
| **Font** | Google Fonts (Prompt) |
| **Animation** | AOS (Animate On Scroll) |

## โครงสร้างโปรเจค

```
myproject/
├── manage.py
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── myapp/
│   ├── models.py          # Model: Client (company_name, website, package, budget, status, date)
│   ├── views.py           # Views: index, services, clients CRUD, search, contact
│   ├── urls.py            # URL routing
│   └── admin.py           # Admin registration
├── templates/
│   ├── base.html          # Base layout (Navbar + Footer)
│   ├── index.html         # Landing page
│   ├── services.html      # Services + Pricing
│   ├── clients.html       # Client management dashboard
│   ├── client_form.html   # Add client form
│   ├── client_edit.html   # Edit client form
│   ├── about.html         # About company
│   └── contact.html       # Contact page
└── requirements.txt
```

## การติดตั้งและตั้งค่า

### 1. Clone โปรเจค

```bash
git clone https://github.com/<username>/digirank-seo.git
cd digirank-seo
```

### 2. สร้าง Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. ติดตั้ง Dependencies

```bash
pip install django
```

### 4. Migration ฐานข้อมูล

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. สร้าง Superuser (สำหรับ Admin)

```bash
python manage.py createsuperuser
```

### 6. รันเซิร์ฟเวอร์

```bash
python manage.py runserver
```

### 7. เปิดเว็บไซต์

- หน้าเว็บ: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## หน้าเว็บไซต์

### หน้าแรก (Landing Page)
![หน้าแรก](screenshots/home.png)
<img width="1692" height="899" alt="Screenshot 2569-04-03 at 15 01 54" src="https://github.com/user-attachments/assets/f3589134-8d22-4c38-b22d-b5c519762b02" />

### หน้าบริการ + แพ็คเกจ
![บริการ](screenshots/services.png)
<img width="1692" height="899" alt="Screenshot 2569-04-03 at 15 02 17" src="https://github.com/user-attachments/assets/4e9b3c73-2cd2-4cc3-bcdd-e304c289e01e" />

### หน้าจัดการลูกค้า (CRUD + ค้นหา)
![ลูกค้า](screenshots/clients.png)
<img width="1692" height="899" alt="Screenshot 2569-04-03 at 15 02 35" src="https://github.com/user-attachments/assets/c2d9c755-430c-41aa-a5c7-731c35c61b65" />

### ฟอร์มเพิ่ม/แก้ไขลูกค้า
![ฟอร์ม](screenshots/form.png)
<img width="1692" height="899" alt="Screenshot 2569-04-03 at 15 02 50" src="https://github.com/user-attachments/assets/2af0813e-a275-4ae4-8310-704e4b51d6a1" />

### Modal ยืนยันการลบ
![ลบ](screenshots/delete.png)
<img width="1692" height="899" alt="Screenshot 2569-04-03 at 15 03 20" src="https://github.com/user-attachments/assets/d548bf0f-f25a-498a-bf1c-b9a5e507cc0e" />

### หน้าเกี่ยวกับเรา
![เกี่ยวกับ](screenshots/about.png)
<img width="1692" height="899" alt="Screenshot 2569-04-03 at 15 03 33" src="https://github.com/user-attachments/assets/9a7c75b2-641d-4566-9ef9-7fe36c1e05b1" />

### หน้าติดต่อ
![ติดต่อ](screenshots/contact.png)
<img width="1692" height="899" alt="Screenshot 2569-04-03 at 15 03 45" src="https://github.com/user-attachments/assets/3b3f07d1-e64e-4bc5-9079-7b5cc0e20652" />

---

## Database Model

### Client

| Field | Type | Description |
|---|---|---|
| `id` | AutoField | Primary Key |
| `company_name` | CharField(200) | ชื่อบริษัท |
| `website` | CharField(300) | URL เว็บไซต์ |
| `package` | CharField(20) | แพ็คเกจ SEO (basic/standard/premium/enterprise) |
| `budget` | IntegerField | งบประมาณ (บาท) |
| `status` | CharField(20) | สถานะ (active/pending/completed) |
| `date` | DateField | วันที่เพิ่มข้อมูล (auto) |

---

> พัฒนาด้วย Django Framework | รายวิชา ICT12367 SPU
> &copy; 2026 DigiRank SEO Agency
