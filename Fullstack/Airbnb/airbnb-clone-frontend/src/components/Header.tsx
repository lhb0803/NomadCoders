import { Box, Button, HStack, IconButton, useDisclosure } from "@chakra-ui/react";
import { FaAirbnb, FaMoon} from "react-icons/fa";
import LoginModal from "./LoginModal";
import SignupModal from "./SignupModal";

export default function Header() {
  const{ isOpen: isLoginOpen, onClose: onLoginClose, onOpen: onLoginOpen} = useDisclosure();
  const{ isOpen: isSignupOpen, onClose: onSignupClose, onOpen: onSignupOpen} = useDisclosure();
  return (
    <HStack justifyContent={"space-between"} py={5} px={10} borderBottomWidth={1}>
      <Box color="red.500">
        <FaAirbnb size={"48"}/>
      </Box>
      <HStack spacing={"2"}>
        <IconButton variant={"ghost"} aria-label="Toggle dark mode" icon={<FaMoon></FaMoon>}/>
        <Button onClick={onLoginOpen}>Log in</Button>
        <Button onClick={onSignupOpen} colorScheme={"red"}>Sign up</Button>
      </HStack>
      <LoginModal isOpen={isLoginOpen} onClose={onLoginClose}></LoginModal>
      <SignupModal isOpen={isSignupOpen} onClose={onSignupClose}></SignupModal>
    </HStack>
  )
}