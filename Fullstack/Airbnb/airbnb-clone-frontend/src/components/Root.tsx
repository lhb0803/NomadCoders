import { Box, Button, HStack, IconButton, Modal, ModalHeader, ModalOverlay, ModalContent, useDisclosure, ModalCloseButton, ModalBody, ModalFooter, Input, VStack, InputGroup, InputLeftElement } from "@chakra-ui/react";
import { Outlet } from "react-router-dom";
import { FaAirbnb, FaMoon, FaUserAlt, FaKey } from "react-icons/fa";

export default function Root() {
  const{ isOpen, onClose, onOpen} = useDisclosure();
  return (
    <Box>
      <HStack justifyContent={"space-between"} py={5} px={10} borderBottomWidth={1}>
        <Box color="red.500">
          <FaAirbnb size={"48"}/>
        </Box>
        <HStack spacing={"2"}>
          <IconButton variant={"ghost"} aria-label="Toggle dark mode" icon={<FaMoon></FaMoon>}/>
          <Button onClick={onOpen}>Log in</Button>
          <Button colorScheme={"red"}>Sign up</Button>
        </HStack>
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
            </ModalBody>
            <ModalFooter>
              <Button colorScheme="red" w="100%">Log in</Button>
            </ModalFooter>
          </ModalContent>
        </Modal>
      </HStack>
      <Outlet />
    </Box>
  );
}