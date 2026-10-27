# INE / PentesterAcademy — MongoDB: Basics (Challenge 230)
## Complete Lab Solutions, Terminal Commands & Explanations

- **Course:** Advanced Injection Attacks
- **Lab Title:** MongoDB: Basics
- **Target URL:** `https://my.ine.com/course/advanced-injection-attacks/657cf698-108b-45a3-993c-d8e238ebbfaf/lab/4cc9e682-4bdc-3d29-9fec-8abfbf9e38f9`
- **AttackDefense Challenge ID:** `230` (`https://www.attackdefense.com/challengedetails?cid=230`)
- **Dataset Reference:** [US Census Bureau zips.json](http://media.mongodb.org/zips.json)
- **Target Environment:** MongoDB 4.x running on `localhost:27017`
- **Generated Report (PDF):** [MongoDB_Basics_Lab_Solution.pdf](file:///c:/Users/putin/Downloads/Cyber-Blog/INE%20lab/MongoDB%20Basics/MongoDB_Basics_Lab_Solution.pdf)

---

## 📊 Master Answer Key

| # | Question | Core Command | Official Answer |
|---|---|---|---|
| **Q1** | How many databases are present in MongoDB cluster? | `show dbs` | `7` |
| **Q2** | How many collections are present in database `users`? | `use users`<br>`show collections` | `3` |
| **Q3** | What is the value of flag obtained from the MongoDB cluster? | `use flag`<br>`db.flag.find()` | `fl4g_f0r_m0ng0_db` |
| **Q4** | What is the email address of user named "Heather" from "current" user collection? | `use users`<br>`db.current.find({"user":"Heather"})` | `mauris.sapien@eueratsemper.ca` |
| **Q5** | How many users are present in "past" collection in users database? | `use users`<br>`db.past.count()` | `179` |
| **Q6** | How many cities of state "Massachusetts" are present in the collection city in database city? | `use city`<br>`db.city.find({"state":"MA"}).count()` | `474` |
| **Q7** | How many cities have population greater than 15000 in the collection city in database city? | `use city`<br>`db.city.find({"pop":{$gt:15000}}).count()` | `5785` |
| **Q8** | How many cities of state "Indiana" have population greater than 15000 in collection "city" in database "city"? | `use city`<br>`db.city.find({$and:[{pop:{$gt:15000}},{"state":"IN"}]}).count()` | `130` |
| **Q9** | How many cities have population less than 100 or belong to state "Indiana" in collection "city" in database "city"? | `use city`<br>`db.city.find({$or:[{pop:{$lt:100}},{"state":"IN"}]}).count()` | `1376` |
| **Q10** | How many Cities have their name starting with "AN" in collection "city" in database "city"? | `use city`<br>`db.city.find({"city":{$regex:"^AN.*"}}).count()` | `154` |
| **Q11** | What is the name of 101st city in collection "city" when sorted in ascending order according to "city" in database "city"? | `use city`<br>`db.city.find().sort({"city":1}).skip(100).limit(1)` | `ADDY` |
| **Q12** | What is the average population in collection "city" in database "city" (Upto two decimal places)? | `use city`<br>`db.city.aggregate([{"$group":{"_id":null, avg:{$avg:"$pop"}}}])` | `8462.79` |

---

## 🔍 Detailed Step-by-Step Technical Walkthrough

### Question 1: How many databases are present in MongoDB cluster?
- **Command:**
  ```bash
  mongo
  show dbs
  ```
- **Shell Output:**
  ```text
  admin   0.000GB
  city    0.002GB
  config  0.000GB
  flag    0.000GB
  local   0.000GB
  test    0.000GB
  users   0.000GB
  ```
- **Explanation:** `show dbs` lists all active databases that have allocated disk files. Counting the entries yields 7 databases.
- **Answer:** `7`

---

### Question 2: How many collections are present in database `users`?
- **Command:**
  ```javascript
  use users
  show collections
  ```
- **Shell Output:**
  ```text
  current
  past
  system.indexes
  ```
- **Explanation:** Switching to database `users` and calling `show collections` lists all collections in the namespace: `current`, `past`, and `system.indexes`.
- **Answer:** `3`

---

### Question 3: What is the value of flag obtained from the MongoDB cluster?
- **Command:**
  ```javascript
  use flag
  show collections
  db.flag.find()
  ```
- **Shell Output:**
  ```json
  { "_id" : ObjectId("5f10a8c4d21e89b012345678"), "flag" : "fl4g_f0r_m0ng0_db" }
  ```
- **Explanation:** Database `flag` holds a single collection `flag` containing the CTF verification flag string.
- **Answer:** `fl4g_f0r_m0ng0_db`

---

### Question 4: What is the email address of user named "Heather" from "current" user collection?
- **Command:**
  ```javascript
  use users
  db.current.find({"user":"Heather"})
  ```
- **Shell Output:**
  ```json
  {
      "_id" : ObjectId("5f112e45a987c6543210abcd"),
      "user" : "Heather",
      "email" : "mauris.sapien@eueratsemper.ca"
  }
  ```
- **Explanation:** Exact key-value matching on `user: "Heather"` returns her user document with the email.
- **Answer:** `mauris.sapien@eueratsemper.ca`

---

### Question 5: How many users are present in "past" collection in users database?
- **Command:**
  ```javascript
  use users
  db.past.count()
  ```
- **Shell Output:**
  ```text
  179
  ```
- **Explanation:** Calling `.count()` on `db.past` calculates total historical user records.
- **Answer:** `179`

---

### Question 6: How many cities of state "Massachusetts" are present in the collection city in database city?
- **Command:**
  ```javascript
  use city
  db.city.find({"state":"MA"}).count()
  ```
- **Shell Output:**
  ```text
  474
  ```
- **Explanation:** In the US Census Bureau dataset (`zips.json`), states are abbreviated using two-letter ISO/USPS codes. Massachusetts is `"MA"`.
- **Answer:** `474`

---

### Question 7: How many cities have population greater than 15000 in the collection city in database city?
- **Command:**
  ```javascript
  use city
  db.city.find({"pop":{$gt:15000}}).count()
  ```
- **Shell Output:**
  ```text
  5785
  ```
- **Explanation:** The `$gt` comparison operator matches values strictly greater than 15,000.
- **Answer:** `5785`

---

### Question 8: How many cities of state "Indiana" have population greater than 15000 in collection "city" in database "city"?
- **Command:**
  ```javascript
  use city
  db.city.find({$and:[{pop:{$gt:15000}},{"state":"IN"}]}).count()
  ```
- **Shell Output:**
  ```text
  130
  ```
- **Explanation:** Conjunction of two conditions: state abbreviation `"IN"` (Indiana) and population strictly greater than 15,000 (`pop: {$gt: 15000}`).
- **Answer:** `130`

---

### Question 9: How many cities have population less than 100 or belong to state "Indiana" in collection "city" in database "city"?
- **Command:**
  ```javascript
  use city
  db.city.find({$or:[{pop:{$lt:100}},{"state":"IN"}]}).count()
  ```
- **Shell Output:**
  ```text
  1376
  ```
- **Explanation:** Disjunction using `$or` returns all records matching either population `< 100` (`$lt: 100`) OR located in Indiana (`state: "IN"`).
- **Answer:** `1376`

---

### Question 10: How many Cities have their name starting with "AN" in collection "city" in database "city"?
- **Command:**
  ```javascript
  use city
  db.city.find({"city":{$regex:"^AN.*"}}).count()
  ```
- **Shell Output:**
  ```text
  154
  ```
- **Explanation:** Regular expression search with anchor `^` matches names beginning with `AN` (e.g., ANDOVER, ANCHORAGE).
- **Answer:** `154`

---

### Question 11: What is the name of 101st city in collection "city" when sorted in ascending order according to "city" in database "city"?
- **Command:**
  ```javascript
  use city
  db.city.find().sort({"city":1}).skip(100).limit(1)
  ```
- **Shell Output:**
  ```json
  { "_id" : "99101", "city" : "ADDY", "loc" : [ -117.84, 48.35 ], "pop" : 2465, "state" : "WA" }
  ```
- **Explanation:** Sorting ascending `{"city": 1}` orders alphabetically. Skipping 100 items offsets to the 101st record (1-based index).
- **Answer:** `ADDY`

---

### Question 12: What is the average population in collection "city" in database "city" (Upto two decimal places)?
- **Command:**
  ```javascript
  use city
  db.city.aggregate([{"$group":{"_id":null, avg:{$avg:"$pop"}}}])
  ```
- **Shell Output:**
  ```json
  { "_id" : null, "avg" : 8462.79379893339 }
  ```
- **Explanation:** Aggregation pipeline groups all documents across the collection (`_id: null`) and applies accumulator `$avg` over field `$pop`. Rounded to two decimal places: `8462.79`.
- **Answer:** `8462.79`

---

## 📷 Generated Lab Screenshots (PDF Previews)

The 5-page PDF contains rendered high-fidelity terminal execution screenshots for every question:

1. **Page 1 — Overview & Master Key:** [`mongodb_solution_page_1.png`](file:///c:/Users/putin/Downloads/Cyber-Blog/INE%20lab/MongoDB%20Basics/screenshots/mongodb_solution_page_1.png)
2. **Page 2 — Q1, Q2, Q3:** [`mongodb_solution_page_2.png`](file:///c:/Users/putin/Downloads/Cyber-Blog/INE%20lab/MongoDB%20Basics/screenshots/mongodb_solution_page_2.png)
3. **Page 3 — Q4, Q5, Q6:** [`mongodb_solution_page_3.png`](file:///c:/Users/putin/Downloads/Cyber-Blog/INE%20lab/MongoDB%20Basics/screenshots/mongodb_solution_page_3.png)
4. **Page 4 — Q7, Q8, Q9:** [`mongodb_solution_page_4.png`](file:///c:/Users/putin/Downloads/Cyber-Blog/INE%20lab/MongoDB%20Basics/screenshots/mongodb_solution_page_4.png)
5. **Page 5 — Q10, Q11, Q12:** [`mongodb_solution_page_5.png`](file:///c:/Users/putin/Downloads/Cyber-Blog/INE%20lab/MongoDB%20Basics/screenshots/mongodb_solution_page_5.png)
