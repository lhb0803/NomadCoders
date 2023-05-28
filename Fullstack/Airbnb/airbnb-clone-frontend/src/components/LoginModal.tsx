import { 
  Modal, ModalOverlay, ModalContent, ModalHeader, ModalCloseButton, ModalBody, 
  VStack, Box, Button, 
  InputGroup, InputLeftElement, Input
} from "@chakra-ui/react"
import { FaUserAlt, FaKey } from "react-icons/fa";
import SocialLogin from "./SocialLogin";

interface LoginModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export default function LoginModal({ isOpen, onClose }: LoginModalProps){
  return (
  <Modal motionPreset={"slideInRight"} isOpen={isOpen} onClose={onClose}>
    <ModalOverlay />
    <ModalContent>
      <ModalHeader>Log in</ModalHeader>
      <ModalCloseButton/>
      <ModalBody>
        <VStack>
          <InputGroup>
            <InputLeftElement children={<Box color={"gray.500"}><FaUserAlt/></Box>}/>
            <Input variant={"filled"} placeholder="Username"/>
          </InputGroup>
          <InputGroup>
            <InputLeftElement children={<Box color={"gray.500"}><FaKey/></Box>}/>
            <Input variant={"filled"} placeholder="Password"/>
          </InputGroup>
        </VStack>
        <Button mt={4} colorScheme="red" w="100%">Log in</Button>
        <SocialLogin></SocialLogin>
      </ModalBody>
    </ModalContent>
  </Modal>
  )
}