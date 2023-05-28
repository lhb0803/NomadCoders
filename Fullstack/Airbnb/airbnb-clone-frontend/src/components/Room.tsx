import { VStack, Box, Image, Button, Grid, Text, HStack, useColorModeValue } from "@chakra-ui/react"
import { FaRegHeart, FaStar } from "react-icons/fa"

interface RoomProps {
  imageUrl: string, 
  name: string, 
  rating: number, 
  city: string,
  country: string, 
  price: number
}

export default function Room({imageUrl, name, rating, city, country, price}: RoomProps){
  const gray = useColorModeValue("gray.600", "gray.300");
  return (
    <VStack alignItems={"flex-start"} spacing="0.5">
      <Box position={"relative"} overflow="hidden" rounded={"xl"} mb={2}>
        <Image minH="280" src={imageUrl}/>
        <Button variant={"unstyled"} position={"absolute"} top={0} right={0} color={"white"}>
          <FaRegHeart size="24px"/>
        </Button>
      </Box>
      <Grid gap="2" templateColumns={"6fr 1fr"}>
        <Text as="b" fontSize="md" noOfLines={1}>
          {name}
        </Text>
        <HStack _hover={{
            color:"gray.500"
          }} spacing={1} alignItems="center">
          <FaStar size="15px"/>
          <Text>{rating}</Text>
        </HStack>
      </Grid>
      <Text fontSize={"sm"} color={gray}>
        {city}, {country}
      </Text>
      <Text fontSize={"sm"} color={gray} >
        <Text as="b">₩{price}</Text>/ night
      </Text>
    </VStack>
  )
}