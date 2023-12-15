using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class cameraMove : MonoBehaviour
{
    public GameObject Player;

    // Update is called once per frame
    void Update()
    {
        transform.position = new Vector3(Mathf.Lerp(transform.position.x, Player.transform.position.x, Time.deltaTime),
           Mathf.Lerp(transform.position.y, Player.transform.position.y, Time.deltaTime),transform.position.z);

    }
}
