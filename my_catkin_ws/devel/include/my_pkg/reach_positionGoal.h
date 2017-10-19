// Generated by gencpp from file my_pkg/reach_positionGoal.msg
// DO NOT EDIT!


#ifndef MY_PKG_MESSAGE_REACH_POSITIONGOAL_H
#define MY_PKG_MESSAGE_REACH_POSITIONGOAL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace my_pkg
{
template <class ContainerAllocator>
struct reach_positionGoal_
{
  typedef reach_positionGoal_<ContainerAllocator> Type;

  reach_positionGoal_()
    : x(0)
    , y(0)  {
    }
  reach_positionGoal_(const ContainerAllocator& _alloc)
    : x(0)
    , y(0)  {
  (void)_alloc;
    }



   typedef int32_t _x_type;
  _x_type x;

   typedef int32_t _y_type;
  _y_type y;




  typedef boost::shared_ptr< ::my_pkg::reach_positionGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::my_pkg::reach_positionGoal_<ContainerAllocator> const> ConstPtr;

}; // struct reach_positionGoal_

typedef ::my_pkg::reach_positionGoal_<std::allocator<void> > reach_positionGoal;

typedef boost::shared_ptr< ::my_pkg::reach_positionGoal > reach_positionGoalPtr;
typedef boost::shared_ptr< ::my_pkg::reach_positionGoal const> reach_positionGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::my_pkg::reach_positionGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::my_pkg::reach_positionGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace my_pkg

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'my_pkg': ['/home/virgile/workspace/groneROSworkshop/my_catkin_ws/devel/share/my_pkg/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::my_pkg::reach_positionGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::my_pkg::reach_positionGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::my_pkg::reach_positionGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::my_pkg::reach_positionGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::my_pkg::reach_positionGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::my_pkg::reach_positionGoal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::my_pkg::reach_positionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bd7b43fd41d4c47bf5c703cc7d016709";
  }

  static const char* value(const ::my_pkg::reach_positionGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xbd7b43fd41d4c47bULL;
  static const uint64_t static_value2 = 0xf5c703cc7d016709ULL;
};

template<class ContainerAllocator>
struct DataType< ::my_pkg::reach_positionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "my_pkg/reach_positionGoal";
  }

  static const char* value(const ::my_pkg::reach_positionGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::my_pkg::reach_positionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
#goal definition\n\
int32 x\n\
int32 y\n\
";
  }

  static const char* value(const ::my_pkg::reach_positionGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::my_pkg::reach_positionGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x);
      stream.next(m.y);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct reach_positionGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::my_pkg::reach_positionGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::my_pkg::reach_positionGoal_<ContainerAllocator>& v)
  {
    s << indent << "x: ";
    Printer<int32_t>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<int32_t>::stream(s, indent + "  ", v.y);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MY_PKG_MESSAGE_REACH_POSITIONGOAL_H
