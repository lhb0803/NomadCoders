import { VStack, Box, Image, Button, Grid, Text, HStack, useColorModeValue } from "@chakra-ui/react"
import { FaRegHeart, FaStar } from "react-icons/fa"

export default function Room(){
  const gray = useColorModeValue("gray.600", "gray.300");
  return (
    <VStack alignItems={"flex-start"} spacing="0.5">
      <Box position={"relative"} overflow="hidden" rounded={"xl"} mb={2}>
        <Image minH="280" src="https://static.stereogum.com/uploads/2015/11/oasis1.jpg"/>
        <Button variant={"unstyled"} position={"absolute"} top={0} right={0} color={"white"}>
          <FaRegHeart size="24px"/>
        </Button>
      </Box>
      <Grid gap="2" templateColumns={"6fr 1fr"}>
        <Text as="b" fontSize="md" noOfLines={1}>
          Oasis: English rock band formed in Manchester in 1991
        </Text>
        <HStack _hover={{
            color:"gray.500"
          }} spacing={1} alignItems="center">
          <FaStar size="15px"/>
          <Text>5.0</Text>
        </HStack>
      </Grid>
      <Text fontSize={"sm"} color={gray}>
        Manchester, UK
      </Text>
      <Text fontSize={"sm"} color={gray} >
        <Text as="b">₩7,000</Text>/ night
      </Text>
    </VStack>
  )
}