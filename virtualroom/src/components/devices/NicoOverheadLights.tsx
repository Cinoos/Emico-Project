"use client"
import React, { useState, useEffect } from "react"

type LightState = {
  on: boolean
  color: string
  brightness: number
}

const DEFAULT_LIGHT_STATE: LightState = {
  on: false,
  color: "#ffffff",
  brightness: 100
}

export default function NicoOverheadLights() {
  const [light, setLight] = useState(DEFAULT_LIGHT_STATE)

  useEffect(()=>{
    async function loadLight(){
        const response = await fetch("/api/devices/overhead-light")
        const data = await response.json()
        setLight(data)
    }
    loadLight()
    //calls loadLight every 1 second
    const poll = setInterval(()=>{
        loadLight()
    },1000)

  },[])

  return (
    <div
  style={{
    width: "120px",
    height: "200px",
    borderRadius: "8px",
    position: "absolute",
    top: "190px",
    left: "50%",
    transform: "translateX(-50%)",

    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    gap: "10px",

    backgroundColor: light.on ? light.color : "#444",
    opacity: light.on ? light.brightness / 100 : 0.3,
  }}
>

  {/* on/off switch */}
  <button
    onClick={() =>
      setLight(prev => ({ ...prev, on: !prev.on }))
    }
    style={{
      padding: "4px 8px",
      fontSize: "11px",
      cursor: "pointer",
      color: light.on ? "black" : "black",
    }}
  >
    {light.on ? " | " : " O "}
  </button>

{/* brightness slider */}
  <input
        type="range"
        min="5"
        max="100"
        value={light.brightness}
        onChange={(e) =>
          setLight(prev => ({
            ...prev,
            brightness: Number(e.target.value)
          }))
        }
        style={{ width: "50%" }}
      />

{/* color */}
<input
  type="color"
  value={light.color}
  onChange={(e) =>
    setLight(prev => ({
      ...prev,
      color: e.target.value
    }))
  }
/>

</div>
  )
}