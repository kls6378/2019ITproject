const express = require('express')
const router = express.Router()

router.get('/',(req,res)=>{
    res.render('main',{name:"효승"})
})

module.exports = router