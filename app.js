const express = require('express')
const app = express()

const bodyParser = require('body-parser')
const session = require('express-session')
const passport = require('passport')
const LocalStrategy = require('passport-local')

const low = require('lowdb')
const FileSync = require('lowdb/adapters/FileSync')
const adapter = new FileSync('db.json')
const db = low(adapter)

const mainRouter = require('./routes/main')

const port = 3000

app.use(session({
  secret: "keyboard cat",
  resave: false,
  saveUninitialized: true
}))
app.use(bodyParser.urlencoded({extended:false}))
app.use(passport.initialize())
app.use(passport.session())

db.defaults({user:[]}).write()

passport.serializeUser((user,done)=>{
  console.log(`serializeUser : ${user}`)
  // done(null, user.id)
})

passport.deserializeUser((id,done)=>{
  console.log(`deserialize : ${id}`)
})

passport.use(new LocalStrategy(
  function (username, password, done){
    console.log(`localStrategy : ${username}, ${password}`)
    db.get('user').find({name:username}).value()
  }
))

app.set('view engine','pug')
app.set('views','views')

app.use('/',mainRouter)

app.listen(3000, function () {
  console.log(`Listening on port ${port}!`)
})