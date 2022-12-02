import express from 'express';
import cors from 'cors';
const app = express();
let styles = {};
app.use(express.json());
app.use(cors());

app.post("/",(req,res)=>{
    try{
        styles = req.body;
        console.log(styles);
        res.send(styles).status(200);
    }catch(err){
        res.send({"ERROR":"Invalid inputs"}).status(500)
    }})



app.get("/",(req,res)=>{
    res.send(styles).status(200);
})

app.listen(3000,()=>{
    console.log("Listenning on port 3000")
})


