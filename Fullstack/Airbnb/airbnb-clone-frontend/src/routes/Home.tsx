import { Box, Grid, Heading, Image, VStack, Text, HStack, Button, Skeleton, SkeletonText } from "@chakra-ui/react";
import { FaStar, FaRegHeart } from "react-icons/fa";
import Room from "../components/Room";
import RoomSkeleton from "../components/RoomSkeleton";

import { useQuery } from "@tanstack/react-query";
import { getRooms } from "../api";
import { Link } from "react-router-dom";
import { IRoomList } from "../types";

export default function Home() {
  const { isLoading, data } = useQuery<IRoomList[]>(["rooms"], getRooms);
  
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
      {data?.map(room => 
        <Room 
          id={room.id}
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