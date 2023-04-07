-- 코드를 입력하세요
select member_id, member_name, gender, to_char(date_of_birth, 'YYYY-MM-DD') AS DATE_OF_BIRTH
from member_profile
where tlno is not null
and EXTRACT(MONTH FROM DATE_OF_BIRTH) = '3'
AND GENDER = 'W'
order by member_id