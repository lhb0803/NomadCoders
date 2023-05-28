import { Box, Grid, Heading, Image, VStack, Text, HStack, Button } from "@chakra-ui/react";
import { FaStar, FaRegHeart } from "react-icons/fa";
import Room from "../components/Room";

export default function Home() {
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
      {[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1].map((index) => (
        <Room key={index}></Room>
      ))}
    </Grid>
  );
}