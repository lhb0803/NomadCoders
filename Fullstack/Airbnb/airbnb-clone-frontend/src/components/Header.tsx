import { Avatar, Box, Button, HStack, IconButton, LightMode, useColorMode, useColorModeValue, useDisclosure } from "@chakra-ui/react";
import { FaAirbnb, FaMoon, FaSun} from "react-icons/fa";
import LoginModal from "./LoginModal";
import SignupModal from "./SignupModal";
import useUser from "../lib/useUser";

export default function Header() {
  const{userLoading, user, isLoggedIn} = useUser();
  const{ isOpen: isLoginOpen, onClose: onLoginClose, onOpen: onLoginOpen} = useDisclosure();
  const{ isOpen: isSignupOpen, onClose: onSignupClose, onOpen: onSignupOpen} = useDisclosure();
  const{ colorMode, toggleColorMode} = useColorMode();
  const logoColor = useColorModeValue("red.500", "red.200");
  const Icon = useColorModeValue(FaMoon, FaSun)
  return (
    <HStack 
      justifyContent={"space-between"} 
      alignItems={"center"}
      py={5} 
      px={10} 
      direction={{
        sm: "column",
        md: "row"
      }}
      spacing={{
        sm: 4,
        md: 6
      }}
      borderBottomWidth={1}
    >
      <Box color={logoColor}>
        <FaAirbnb size={"48"}/>
      </Box>
      <HStack spacing={"2"}>
        <IconButton 
          onClick={toggleColorMode}
          variant={"ghost"} 
          aria-label="Toggle dark mode" 
          icon={<Icon/>}
        />
        {userLoading ? null : !isLoggedIn ? <>
          <Button onClick={onLoginOpen}>Log in</Button>
          <LightMode>
            <Button onClick={onSignupOpen} colorScheme={"red"}>Sign up</Button>
          </LightMode>
          </> 
          : <Avatar size={"md"}/>
        }
      </HStack>
      <LoginModal isOpen={isLoginOpen} onClose={onLoginClose}></LoginModal>
      <SignupModal isOpen={isSignupOpen} onClose={onSignupClose}></SignupModal>
    </HStack>
  )
}