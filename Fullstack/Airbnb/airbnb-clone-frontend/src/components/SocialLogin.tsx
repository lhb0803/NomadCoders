import {Box, HStack, VStack, Text, Divider, Button} from "@chakra-ui/react"
import { FaComment, FaGithub } from "react-icons/fa";

export default function SocialLogin() {
 return (
  <Box mb={4}>
    <HStack my={4}>
      <Divider />
      <Text textTransform={"uppercase"} color="gray.500" fontSize="xs" as="b">Or</Text>
      <Divider />
    </HStack>
    <VStack>
      <Button leftIcon={<FaGithub/>}colorScheme="telegram" w="100%">Continue with Github</Button>
      <Button leftIcon={<FaComment/>} colorScheme="yellow" w="100%">Continue with Kakao</Button>
    </VStack>
  </Box>
 )
}