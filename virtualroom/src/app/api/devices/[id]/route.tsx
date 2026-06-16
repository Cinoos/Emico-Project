import { NextResponse } from 'next/server'

type LightState = {
    on:boolean;
    color:string;
    brightness:number;
}

const devices: Record<string,LightState> = {
"overhead-light": {
    on:false,
    color:"#fffff",
    brightness:100,
},
"desk-lamp": {
    on:false,
    color:"#fffff",
    brightness:100,
},

}

export async function GET(request: Request, context:any) 
{
   const { id } = await context.params
   const device =  devices[id]
   return NextResponse.json(device)
}

export async function POST(request: Request, context:any) 
{
   const { id } = await context.params
   const device =  devices[id]

   const newState = await request.json()
   const oldState = devices[id]
   devices[id] = {
    ...devices[id],
    ...newState
   }

   console.log("we've been hit!")
   console.log(oldState)
   console.log(devices[id])
   return NextResponse.json({oldState: oldState, newState:devices[id]})
}