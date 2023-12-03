using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Monopoly
{
    public class Card
    {
        enum EventsEnum { GetMoney, PayMoney,Move}
        Dictionary<EventsEnum, int> Events = new Dictionary<EventsEnum, int>();
        string Title = "Rücke vor auf Los";
     
        public Card()
        {
            Events = new Dictionary<EventsEnum, int>();
            Events.Add(EventsEnum.PayMoney, 50);
        }
    }
}
