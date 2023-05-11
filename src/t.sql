select books.bookname, profiels.nickname, reviews.*
from books
inner join reviews
on books.id = reviews.book_id
inner join auth_user
on reviews.created_by_id = auth_user.id
INNER JOIN profiels
ON profiels.id = auth_user.id
where books.id = 1

--related
--books(id=●●) reviews auth_user profiels