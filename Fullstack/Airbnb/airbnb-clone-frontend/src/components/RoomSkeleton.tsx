import { Box, Skeleton, SkeletonText } from "@chakra-ui/react"

export default function RoomSkeleton(){
  return (
    <Box>
      <Skeleton height={280} rounded={"xl"} mb={2}/>
      <SkeletonText w={"50%"} noOfLines={2} mb={2}/>
      <SkeletonText w={"20%"} noOfLines={1}/>
    </Box>
  )
}