SELECT B.BOOK_ID, A.AUTHOR_NAME, TO_CHAR(PUBLISHED_DATE,'YYYY-MM-DD')
FROM AUTHOR A INNER JOIN BOOK B
ON A.AUTHOR_ID=B.AUTHOR_ID
WHERE B.CATEGORY='경제'
ORDER BY B.PUBLISHED_DATE