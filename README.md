# Named Entity Recognition System for Arabic.

The system can annotate the following entities:
1. **PERSON**

-  و هذا ما نفاه المعاون السياسي للرئيس ***نبيه بري*** ، النائب ***علي حسن خليل***   

- لكن أوساط ***الحريري*** تعتبر أنه ضحى كثيرا في سبيل البلد 

- و ستفقد الملكة ***إليزابيث الثانية*** بذلك سيادتها على واحدة من آخر ممالك الكومنولث 

2. **ORGANIZATION**

- حسب أرقام ***البنك الدولي*** 

-  أعلن ***الجيش العراقي*** 

-  و نقلت وكالة ***رويترز*** عن ثلاثة دبلوماسيين في ***الاتحاد الأوروبي*** ، أن ***بلجيكا*** و ***إيرلندا*** و ***لوكسمبورغ*** تريد أيضاً مناقشة 

-  ***الحكومة الاتحادية*** و ***حكومة إقليم كردستان*** 

- و هو ما يثير الشكوك حول مشاركة النجم البرتغالي في المباراة المرتقبة أمام ***برشلونة*** الإسباني في 


3. ***LOCATION***

-  الجديد هو تمكين اللاجئين من “ مغادرة الجزيرة تدريجياً و بهدوء إلى ***أثينا*** ” 

-  ***جزيرة ساكيز*** تبعد 1 كم عن ***إزمير*** 


4. **DATE**

-  ***غدا الجمعة*** 

-  ***06 أكتوبر 2020*** 

- ***العام السابق*** 


5. **PRODUCT**

-  عبر حسابه ب ***تطبيق “ إنستغرام ”*** 

-  الجيل الثاني من ***نظارة الواقع الافتراضي أوكولوس كويست*** تحت اسم " ***أوكولوس كويست 2*** " 


6. **COMPETITION**

-  عدم المشاركة في ***بطولة فرنسا المفتوحة للتنس*** 

-  في مباراة ***كأس السوبر الأوروبي*** 

7. **PRICE**

-  ***جائزة نوبل ل لآداب***

-  الذي فاز ب ***جائزة “ إيمي ” لأفضل دور مساند***

8. **EVENT**

-  تسجّل أغنية جديدة خاصة ب ***العيد الوطني السعودي***

- ***مهرجان المرأة يافوية*** في دورته الرابعة 

9. **DISEASE**

-  في مكافحة فيروس ***كورونا*** و عدد من الأمراض 

-  الأزمات المشابهة مثل “ ***انفلونزا الطيور*** ” و ” ***انفلونزا الخنازير***

## Example
First install the required libraries

```
python3 -m venv venv

```

```
source venv/bin/activate

```

```
pip install -r requirements.txt

```

```
python tagger.py

```

### Input

```
'رغم الهدنة .. معارك قره باغ متواصلة وأذربيجان تعلن سيطرتها على مزيد من القرى'
```


### Output

```
{"text": "رغم الهدنة . . معارك قره باغ متواصلة و أذربيجان تعلن سيطرتها على مزيد من القرى", "entities": [{"type": "LOCATION", "entity": "قره باغ", "start_offset": 21, "end_offset": 28}, {"type": "ORGANIZATION", "entity": "أذربيجان", "start_offset": 39, "end_offset": 47}]}

```

## Training Corpus

The training corpus is made of 378.000 tokens (14.000 sentences) collected from the Web and annotated manually.

## Results

The results on a valid corpus made of 30.000 tokens shows an F-measure of ~87%.
