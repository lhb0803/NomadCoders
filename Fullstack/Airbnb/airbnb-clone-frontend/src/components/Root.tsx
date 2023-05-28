import { Box, Button, HStack, IconButton } from "@chakra-ui/react";
import { Outlet } from "react-router-dom";
import { FaAirbnb, FaMoon } from "react-icons/fa";

export default function Root() {
  return (
    <Box>
      <HStack justifyContent={"space-between"} py={5} px={10} borderBottomWidth={1}>
        <Box color="red.500">
          <FaAirbnb size={"48"}/>
        </Box>
        <HStack spacing={"2"}>
          <IconButton variant={"ghost"} aria-label="Toggle dark mode" icon={<FaMoon></FaMoon>}/>
          <Button>Log in</Button>
          <Button colorScheme={"red"}>Sign up</Button>
        </HStack>
      </HStack>
      <Outlet />
    </Box>
  );
}