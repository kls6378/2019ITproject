const express = require('express')
const app = express()

const port = 3000

app.set('view engine','pug')
app.set('views','views')

app.get('/', function (req, res) {
  res.render('main',{name:'leesu'})
})

app.listen(3000, function () {
  console.log(`Listening on port ${port}!`)
})