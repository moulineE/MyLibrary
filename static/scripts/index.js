$(document).ready(function () {
  $(':input').on('input', async function () {
    const input = $(this);
    if (input.val() === '') {
      $('.booksResult').html('');
      return;
    }
    const response = await fetch('/mylibrary/api/v1/search?q=' + input.val());
    const books = await response.json();
    console.log(books);
    let html = '';
    for (const book of books) {
      let author = (await fetch('/mylibrary/api/v1/authors/' + book.author_id));
      author = await author.json();
      html += `<li><h2><a href="/mylibrary/book?id=${book.id}"> ${book.book_title}</a></h2><h3>${author.first_name + ' ' + author.last_name}</h3><h4>published the ${book.published_date}</h4><p>${book.book_summary}</p></li>`;
    }
    $('UL.booksResult').html(html);
  });
});