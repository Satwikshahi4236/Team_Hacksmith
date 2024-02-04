import { config } from 'dotenv'
config()
import { OpenAI } from 'openai'
import readline from 'readline'


const openai = new OpenAI( { apiKey: process.env.OPENAI_API_KEY } );

const userInterface = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

userInterface.prompt()
userInterface.on("line",async input=>{

   const res = await openai.chat.completions.create({ 
        model: "gpt-3.5-turbo",
         messages: [
             { role: "user", content: input }
         ]
     })
     console.log(res)
      res.choices.forEach( out => console.log(out.message) )
     userInterface.prompt()
})

