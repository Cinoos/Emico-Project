import Image from "next/image";
import NicoRoom from "@/components/rooms/NicoRoom";

export default function Home() {
  return (
    <div>
      <h1>Virtual rooms</h1>
      <NicoRoom/>
    </div>
  );
}
