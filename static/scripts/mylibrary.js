$(document).ready(function () {
  $(':input').change(async function () {
    const input = $(this);
    const response = await fetch('/mylibrary/api/v1/search?q=' + input.val());
    const books = await response.json();
    console.log(books);
    let html = '';
    for (const book of books) {
      let author = (await fetch('/mylibrary/api/v1/authors/' + book.author_id));
      author = await author.json()
      html += `<li><h2>${book.book_title}</h2><h3>${author.first_name +' '+ author.last_name}</h3><h4>${book.book_summary}</h4></li>`;
    }
    $('.booksResults').html(html);
  });
});
