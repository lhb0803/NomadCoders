import { 
  Modal, ModalOverlay, ModalContent, ModalHeader, ModalCloseButton, ModalBody, 
  VStack, Box, Button, 
  InputGroup, InputLeftElement, Input
} from "@chakra-ui/react"
import { FaUserAlt, FaKey, FaEnvelope, FaPen } from "react-icons/fa";

interface SignupModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export default function SignupModal({ isOpen, onClose }: SignupModalProps){
  return (
    <Modal isOpen={isOpen} onClose={onClose}>
      <ModalOverlay />
      <ModalContent>
        <ModalHeader>Sign up</ModalHeader>
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
            <InputGroup>
              <InputLeftElement children={<Box color={"gray.500"}><FaPen/></Box>}/>
              <Input variant={"filled"} placeholder="Name"/>
            </InputGroup>
            <InputGroup>
              <InputLeftElement children={<Box color={"gray.500"}><FaEnvelope/></Box>}/>
              <Input variant={"filled"} placeholder="Email"/>
            </InputGroup>
          </VStack>
          <Button mt={4} colorScheme="red" w="100%">Sign up</Button>

        </ModalBody>
      </ModalContent>
    </Modal>
  );
}