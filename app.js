const express = require('express')
const app = express()

const port = 3000

const mainRouter = require('./routes/main')

app.set('view engine','pug')
app.set('views','views')

app.use('/',mainRouter)

app.listen(3000, function () {
  console.log(`Listening on port ${port}!`)
})