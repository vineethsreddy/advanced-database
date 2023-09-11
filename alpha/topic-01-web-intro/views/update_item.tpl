<html>
<body>
<hr/>
<form action="/update" method="post">
  <p>ID:<input name="id" value={{str(item['id'])}}><input>
  <p>Description:<input name="description" value={{item['description']}}/></p>
  <p><button type="submit">Submit</button></p>
<form>
<hr/>
<body>
</html>