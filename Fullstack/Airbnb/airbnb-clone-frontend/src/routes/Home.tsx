import { Box, Grid, Heading, Image, VStack, Text, HStack } from "@chakra-ui/react";
import { FaStar } from "react-icons/fa";

export default function Home() {
  return (
    <Grid 
      mt={10}
      px={10}
      columnGap={4} 
      rowGap={8} 
      templateColumns={"repeat(4, 1fr)"}
    >
      <Box>
        <Box overflow="hidden" rounded={"xl"} mb={2}>
            <Image h="280" src="https://static.stereogum.com/uploads/2015/11/oasis1.jpg"/>
        </Box>
        <VStack alignItems={"flex-start"} spacing="0.5">
          <Grid gap="2" templateColumns={"6fr 1fr"}>
            <Text as="b" fontSize="md" noOfLines={1}>
              Oasis: English rock band formed in Manchester in 1991
            </Text>
            <HStack>
              <FaStar size="15px"/>
              <Text>5.0</Text>
            </HStack>
          </Grid>
          <Text fontSize={"sm"} color={"gray.500"}>
            Manchester, UK
          </Text>
          <Text fontSize={"sm"} color={"gray.500"} >
            <Text as="b">₩7,000</Text>/ night
          </Text>
        </VStack>
      </Box>
    </Grid>
  );
}