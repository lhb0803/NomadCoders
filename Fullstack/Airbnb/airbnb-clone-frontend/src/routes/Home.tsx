import { Box, Grid, Heading, Image, VStack, Text, HStack, Button, Skeleton, SkeletonText } from "@chakra-ui/react";
import { FaStar, FaRegHeart } from "react-icons/fa";
import Room from "../components/Room";
import RoomSkeleton from "../components/RoomSkeleton";
import { useEffect, useState } from "react";

interface IPhoto {
  "pk": number,
  "file": string,
  "description": string
}

interface IRoom {
  "id": number,
  "name": string,
  "country": string,
  "city": string,
  "price": number,
  "rating": number,
  "is_owner": boolean,
  "photos": IPhoto[]
}

export default function Home() {
  const [isLoading, setIsLoading] = useState(true);
  const [rooms, setRooms] = useState<IRoom[]>([]);
  const fetchRooms = async() => {
    const response = await fetch("http://127.0.0.1:8000/api/v1/rooms/");
    const json = await response.json();
    setRooms(json)
    setIsLoading(false)
  }
  useEffect(() => {
    fetchRooms();
  },[])
  return (
    <Grid 
      mt={10}
      px={{
        base: "1",
        lg: "4"
      }}
      columnGap={4} 
      rowGap={8} 
      templateColumns={{
        sm: "1fr",
        md: "1fr 1fr",
        lg: "repeat(3, 1fr)",
        xl: "repeat(4, 1fr)",
        "2xl": "repeat(5, 1fr)",
      }}
    >
      {isLoading ? (
        <>
        <RoomSkeleton/>
        </>
      ) : null}
      {rooms.map(room => 
        <Room 
          imageUrl={room.photos[0].file}
          name={room.name}
          rating={room.rating}
          city={room.city}
          country={room.country}
          price={room.price}
        />
      )}
    </Grid>
  );
}